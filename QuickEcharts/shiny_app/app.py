from shiny import App, reactive, render, ui
from QuickEcharts import Charts
import polars as pl
import logging
from .modules.schemas import PLOT_SCHEMAS 


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_dark_mode(id="light_dark_mode", mode="dark"),
        ui.input_action_button("build_plot", ui.HTML('<i class="fa fa-bar-chart"></i> Build Plot')),
        ui.input_file("dt", "Upload Data Table"),
        ui.input_select("plot_type", "Select Plot Type", choices=list(PLOT_SCHEMAS.keys()), selected="Area"),
        ui.output_ui("dynamic_inputs")
    ),
    ui.card(
        ui.card_header("Dynamic Plot Viewer", class_="bg-primary text-white"),  # Add styling classes
        ui.output_text_verbatim("columns"),
        ui.output_ui("plot"),
    ),
    title = "QuickEcharts"
)


def server(input, output, session):
    @reactive.calc
    def load_data():
        """Load the uploaded data as a Polars DataFrame."""
        if input.dt() is None:
            logger.info("No data uploaded yet.")
            return None
        try:
            file_info = input.dt()[0]
            file_path = file_info["datapath"]
            logger.info(f"Loading data from: {file_path}")
            df = pl.read_csv(file_path)
            return df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return None

    @reactive.effect
    def update_dropdowns():
        """Update dropdowns based on the loaded data."""
        data = load_data()
        if data is not None:
            columns = data.columns
            plot_type = input.plot_type()
            if plot_type:
                schema = PLOT_SCHEMAS.get(plot_type, {})
                for param, param_info in schema.items():
                    if "Variable" in param_info.get("label", ""):
                        ui.update_select(param, choices=["None"] + columns)
        else:
            logger.info("No data to update dropdowns.")

    @output
    @render.text
    def columns():
        """Display the loaded data's columns for debugging."""
        data = load_data()
        if data is not None:
            return None
        return "No data loaded yet."

    @output
    @render.ui
    def dynamic_inputs():
        """Generate dynamic inputs based on the selected plot type schema."""
        plot_type = input.plot_type()
        if not plot_type:
            logger.info("No plot type selected yet.")
            return ui.p("Please select a plot type.")

        schema = PLOT_SCHEMAS.get(plot_type, {})
        inputs = []
        for param, param_info in schema.items():
            input_id = param
            label = param_info.get("label", param)
            default = param_info.get("default", None)

            if param_info["type"] == "text":
                inputs.append(ui.input_text(input_id, label, value=default or ""))
            elif param_info["type"] == "checkbox":
                inputs.append(ui.input_checkbox(input_id, label, value=default or False))
            elif param_info["type"] == "slider":
                inputs.append(
                    ui.input_slider(
                        input_id, label, param_info["min"], param_info["max"], value=default or param_info["min"]
                    )
                )
            elif param_info["type"] == "select":
                if "Variable" in label:
                    inputs.append(
                        ui.input_select(
                            input_id, label, choices=[]
                        )  # Choices will be updated dynamically
                    )
                else:
                    inputs.append(
                        ui.input_select(
                            input_id, label, choices=param_info.get("options", []), selected=default
                        )
                    )

            elif param_info["type"] == "multi-select":
                inputs.append(
                    ui.input_select(
                        input_id,
                        label,
                        choices=param_info.get("options", []),
                        selected=default,
                        multiple=True  # Allow multiple selections
                    )
                )
        return inputs

    @output
    @render.ui
    def plot():
        """Render the plot based on user inputs and selected plot type."""
        logger.info(f"Plotting step 1")
        if input.build_plot() == 0:
            return ui.p("Click 'Build Plot' to generate the plot.")
        
        # Load data (assuming this is a synchronous operation)
        logger.info(f"Plotting step 2: data loading")
        data = load_data()
        if data is None:
            return ui.p("Please upload a data file.")
        
        plot_type = input.plot_type()
        if not plot_type:
            return ui.p("Please select a plot type.")
        
        try:
            # Collect parameters dynamically
            logger.info(f"Plotting step 3")
            schema = PLOT_SCHEMAS[plot_type]
            params = {}
            for param in schema.keys():
                logger.info(f"Plotting step 4")
                value = input[param]() if callable(input[param]) else input[param]
                if param in ["FacetRows", "FacetCols"]:
                    # Convert FacetRows and FacetCols to integers
                    params[param] = int(value) if value not in ["None", ""] else None
                elif param == 'dt':
                    params[param] = data
                elif isinstance(value, (list, tuple)) and len(value) > 1:  # Check for multiple elements
                    # Convert multiple elements to a list
                    params[param] = list(value)
                elif isinstance(value, tuple) and len(value) == 1:  # Check for single-element tuple
                    # Unpack single-element tuple
                    params[param] = value[0]
                else:
                    # Keep single values as they are
                    params[param] = value if value not in ["None", ""] else None

            # Create plot dynamically using the selected plot function
            logger.info(f"Plotting step 5")
            plot_function = getattr(Charts, plot_type)
            logger.info(f"Creating {plot_type} plot with parameters: {params}")
            def replace_title_in_html(html):
                # Replace the title
                updated_html = html.replace("<title>Awesome-pyecharts</title>", "<title>QuickEcharts App</title>")
                # Add JavaScript for reinitialization
                updated_html += """
                <script>
                setTimeout(() => {
                    // Ensure ECharts is available
                    if (typeof echarts !== 'undefined') {
                        // Select the chart container
                        const chartContainer = document.getElementById('chart');
                        if (chartContainer) {
                            // Dispose of existing chart instance
                            const instance = echarts.getInstanceByDom(chartContainer);
                            if (instance) instance.dispose();
            
                            // Reinitialize with the updated theme
                            echarts.init(chartContainer);
                        }
                    }
                }, 100);
                </script>
                """
                return updated_html


            # Generate the plot (assumes synchronous plot function)
            if not hasattr(plot, "has_run"):
                reactive.invalidate_later(0.1)
                plot.has_run = True  # Prevent further invalidation loops
            chart = plot_function(**params)
            rendered_file = replace_title_in_html(chart.render_embed())
            return ui.HTML(rendered_file)
        except Exception as e:
            logger.error(f"Error creating plot: {e}")
            return ui.p(f"Error creating plot: {e}")


# App launcher function
def run_app(port=8001):
    app = App(app_ui, server)
    app.run(port=port)
