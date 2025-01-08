# Module: Charts
# Author: Adrian Antico <adrianantico@gmail.com>
# License: APGL (>= 3)
# Release: quickecharts 1.2.0
# Last modified : 2025-01-05

import numpy as np
import polars as pl
import math
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import (
    Timeline,
    Line as PyLine,
    Bar as PyBar,
    Grid,
    Pie as PyPie,
    Boxplot,
    WordCloud as PyWordCloud,
    Radar as PyRadar,
    HeatMap,
    Scatter as PyScatter,
    Scatter3D as PyScatter3D,
    Parallel as PyParallel,
    Funnel as PyFunnel,
    Bar3D as PyBar3D,
    ThemeRiver
 )


def NumericTransformation(dt, YVar, Trans):
  """
  Parameters
  dt: polars dataframe
  YVar: column to transform
  Trans: transformation method. Choose from 'sqrt', 'log', 'logmin', 'asinh', 'perc_rank'
  """
  Trans = Trans.lower()
  if Trans == "sqrt":
    dt = dt.with_columns(pl.col(YVar).sqrt())
  elif Trans == 'log':
    dt = dt.with_columns(pl.col(YVar).log())
  elif Trans == 'asinh':
    dt = dt.with_columns(np.arcsinh(pl.col(YVar)))
  elif Trans == 'logmin':
    dt = dt.with_columns(YVar = dt[YVar] + 1 + dt[YVar].min())
    dt = dt.drop(YVar)
    dt = dt.rename({"YVar": YVar})
    dt = dt.with_columns(pl.col(YVar).log())
  elif Trans == 'perc_rank':
    perc_rank = dt[YVar].rank() / dt[YVar].count()
    dt = dt.drop(YVar)
    dt = dt.with_columns(perc_rank.rename(YVar))
  return dt


def PolarsAggregation(dt, AggMethod, NumericVariable, GroupVariable, DateVariable):
  
  if AggMethod == "count":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).len())
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).len())
    else:
      dt = dt.group_by(DateVariable).agg(pl.col(NumericVariable).len())
  elif AggMethod == "mean":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).mean())
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).mean())
    else:
      dt = dt.group_by(DateVariable).agg(pl.col(NumericVariable).mean())
  elif AggMethod == "sum":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).sum())
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).sum())
    else:
      dt = dt.group_by(DateVariable).agg(pl.col(NumericVariable).sum())
  elif AggMethod == "median":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).median())
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).median())
    else:
      dt = dt.group_by(DateVariable).agg(pl.col(NumericVariable).median())
  elif AggMethod == "sd":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).std())
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).std())
    else:
      dt = dt.group_by(DateVariable).agg(pl.col(NumericVariable).std())
  elif AggMethod == "skewness":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by([GroupVariable, DateVariable]).agg([pl.all().skew()])
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg([pl.all().skew()])
    else:
      dt = dt.group_by(DateVariable).agg([pl.all().skew()])
  elif AggMethod == "kurtosis":
    if not GroupVariable is None and not DateVariable is None:
      dt = dt.group_by([GroupVariable, DateVariable]).agg([pl.all().kurtosis()])
    elif not GroupVariable is None:
      dt = dt.group_by(GroupVariable).agg([pl.all().kurtosis()])
    else:
      dt = dt.group_by(DateVariable).agg([pl.all().kurtosis()])
  elif AggMethod == "CoeffVar":
    if not GroupVariable is None and not DateVariable is None:
      mean = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).mean())
      std = dt.group_by(GroupVariable, DateVariable).agg(pl.col(NumericVariable).std())
      joined = mean.join(std, on = [GroupVariable, DateVariable])
      joined = joined.with_columns((pl.col(NumericVariable) / pl.col(NumericVariable + '_right')).alias(NumericVariable))
      dt = joined.select([pl.col(GroupVariable), pl.col(DateVariable), pl.col(NumericVariable)])
    elif not GroupVariable is None:
      mean = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).mean())
      std = dt.group_by(GroupVariable).agg(pl.col(NumericVariable).std())
      joined = mean.join(std, on = [GroupVariable])
      joined = joined.with_columns((pl.col(NumericVariable) / pl.col(NumericVariable + '_right')).alias(NumericVariable))
      dt = joined.select([pl.col(GroupVariable), pl.col(NumericVariable)])
    else:
      mean = dt.group_by(DateVariable).agg(pl.col(NumericVariable).mean())
      std = dt.group_by(DateVariable).agg(pl.col(NumericVariable).std())
      joined = mean.join(std, on = [DateVariable])
      joined = joined.with_columns((pl.col(NumericVariable) / pl.col(NumericVariable + '_right')).alias(NumericVariable))
      dt = joined.select([pl.col(DateVariable), pl.col(NumericVariable)])
  
  return(dt)


def FacetGridValues(
    FacetRows=1, 
    FacetCols=1, 
    Legend='top', 
    LegendSpace=10, 
    Height="750px", 
    Width="1250px"
):
    """
    Calculates grid options for a facet grid layout using the original percentage-based logic
    with adjustments for total height and width based on FacetRows and FacetCols.

    Parameters:
    - FacetRows (int): Number of rows in the facet grid.
    - FacetCols (int): Number of columns in the facet grid.
    - Legend (str): Position of the legend ('top', 'right', or others).
    - LegendSpace (int): Space allocated for the legend (in percentage).
    - Height (str): Height of the entire grid in pixels.
    - Width (str): Width of the entire grid in pixels.

    Returns:
    - dict: Contains positions (`top`, `left`) and dimensions (`width`, `height`) for each panel.
    """
    # Parse pixel-based dimensions
    total_height_px = int(Height.replace("px", "")) if Height else 750
    total_width_px = int(Width.replace("px", "")) if Width else 1250

    # Convert dimensions to percentages
    total_height_percent = 100
    total_width_percent = 100

    # Specified margins (as percentages)
    margin_trbl = {"t": 2, "r": 2, "b": 5, "l": 5}

    # Calculate spacing adjustments
    v_panel_space = 2  # max(0, 10 - FacetRows)
    h_panel_space = 9  # max(0, 10 - FacetCols)

    # Calculate maximum space for panels
    if Legend == "top":
        w_max = total_width_percent - margin_trbl["l"] - margin_trbl["r"]
        h_max = total_height_percent - LegendSpace - margin_trbl["b"] - margin_trbl["t"]
    elif Legend == "right":
        w_max = total_width_percent - LegendSpace - margin_trbl["l"] - margin_trbl["r"]
        h_max = total_height_percent - margin_trbl["b"] - margin_trbl["t"]
    else:
        w_max = total_width_percent - margin_trbl["l"] - margin_trbl["r"]
        h_max = total_height_percent - margin_trbl["b"] - margin_trbl["t"]

    # Total space for panels, accounting for spacing and legend
    FacetRows_h_max = h_max - (v_panel_space * (max(1, FacetRows * 0.33)))
    FacetCols_w_max = w_max - h_panel_space

    # Dimensions of each panel (in percentages)
    height = FacetRows_h_max / FacetRows
    width = FacetCols_w_max / FacetCols

    # Generate positions from the top
    top_pos_values = [
        margin_trbl["t"] + (row * (height + v_panel_space)) for row in range(FacetRows)
    ]
    top_pos_values_rep = top_pos_values * FacetCols
    top_pos_values_rep.sort()

    # Generate positions from the left
    left_pos_values = [
        margin_trbl["l"] + (col * (width + h_panel_space)) for col in range(FacetCols)
    ]
    left_pos_values_rep = left_pos_values * FacetRows

    return {
        "top": top_pos_values_rep,
        "left": left_pos_values_rep,
        "Width_f": width - 5,  # Subtract 5 for panel adjustments
        "Height_f": height
    }



def Animation(AnimationThreshold, AnimationDuration, AnimationEasing, AnimationDelay, AnimationDurationUpdate, AnimationEasingUpdate, AnimationDelayUpdate):
  options = {}
  options['animation_threshold'] = AnimationThreshold
  options['animation_duration'] = AnimationDuration
  options['animation_easing'] = AnimationEasing
  options['animation_delay'] = AnimationDelay
  options['animation_duration_update'] = AnimationDurationUpdate
  options['animation_easing_update'] = AnimationEasingUpdate
  options['animation_delay_update'] = AnimationDelayUpdate
  return options


def get_toolbox_options():
    """
    Return the standard toolbox options for plots.
    """
    return opts.ToolboxOpts(
        feature=opts.ToolBoxFeatureOpts(
            save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(title="Download as Image"),
            restore=opts.ToolBoxFeatureRestoreOpts(title="Restore"),
            data_view=opts.ToolBoxFeatureDataViewOpts(title="View Data", lang=["Data View", "Close", "Refresh"]),
            data_zoom=opts.ToolBoxFeatureDataZoomOpts(zoom_title="Zoom In", back_title="Zoom Out"),
            magic_type=opts.ToolBoxFeatureMagicTypeOpts(line_title="Line", bar_title="Bar", stack_title="Stack"),
        )
    )


def get_datazoom_options():
    """
    Return the standard datazoom options for plots.
    """
    return [
        opts.DataZoomOpts(
            range_start=0,
            range_end=100
        ),
        opts.DataZoomOpts(
            type_="inside"
        ),
    ]


def get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize):
    """
    Return the title options for plots.

    Parameters:
    - Title: Main title of the plot.
    - SubTitle: Subtitle of the plot.
    - TitleColor: Color of the main title text (default: black).
    - SubTitleColor: Color of the subtitle text (default: gray).
    - TitleFontSize: Font size for the main title (default: 14).
    - SubTitleFontSize: Font size for the subtitle (default: 12).

    Returns:
    - TitleOpts: Configured title options for a chart.
    """
    return opts.TitleOpts(
        title=Title,
        subtitle=SubTitle,
        title_textstyle_opts=opts.TextStyleOpts(
            color=TitleColor,
            font_size=TitleFontSize,
        ),
        subtitle_textstyle_opts=opts.TextStyleOpts(
            color=SubTitleColor,
            font_size=SubTitleFontSize,
        ),
    )


def cap_records(dt, sample_size=None):
    """
    Cap the number of records in a DataFrame based on a given sample size.

    Parameters:
    - dt: The input DataFrame.
    - sample_size: The maximum number of records to keep (if not None).

    Returns:
    - A DataFrame capped at the specified sample size.
    """
    if sample_size is not None:
        if dt.shape[0] > sample_size:
            return dt.sample(n=sample_size, shuffle=True)
        else:
            return dt.clone()
    else:
        return dt.clone()


def initialize_options(
    theme=None,
    width=None,
    height=None,
    background_color=None,
    animation_threshold=None,
    animation_duration=None,
    animation_easing=None,
    animation_delay=None,
    animation_duration_update=None,
    animation_easing_update=None,
    animation_delay_update=None,
):
    """
    Initialize chart options for theme, dimensions, background, and animations.

    Parameters:
    - theme: Theme for the chart (e.g., light, dark).
    - width: Width of the chart (e.g., "600px").
    - height: Height of the chart (e.g., "400px").
    - background_color: Background color of the chart.
    - animation_threshold: Threshold for animations.
    - animation_duration: Duration of the animation.
    - animation_easing: Easing function for the animation.
    - animation_delay: Delay before animation starts.
    - animation_duration_update: Duration for animation updates.
    - animation_easing_update: Easing function for updates.
    - animation_delay_update: Delay before updates start.

    Returns:
    - A dictionary containing initialized options.
    """
    # Initialize options dictionary
    init_options = {}

    # Add optional parameters
    if theme is not None:
        init_options['theme'] = theme
    if width is not None:
        init_options['width'] = width
    if height is not None:
        init_options['height'] = height
    if background_color is not None:
        init_options['bg_color'] = background_color

    # Add default options
    init_options['is_horizontal_center'] = True

    # Add animation options
    animation_options = {
        "animation_threshold": animation_threshold,
        "animation_duration": animation_duration,
        "animation_easing": animation_easing,
        "animation_delay": animation_delay,
        "animation_duration_update": animation_duration_update,
        "animation_easing_update": animation_easing_update,
        "animation_delay_update": animation_delay_update,
    }
    init_options['animation_opts'] = opts.AnimationOpts(**{k: v for k, v in animation_options.items() if v is not None})

    return init_options


def configure_legend_options(
    legend=None,
    legend_pos_right=None,
    legend_pos_top=None,
    legend_border_size=None,
    legend_text_color=None,
):
    """
    Configure the legend options for a chart.

    Parameters:
    - legend: Position of the legend ('right', 'top', or None for hidden).
    - legend_pos_right: Position of the legend from the right (if applicable).
    - legend_pos_top: Position of the legend from the top.
    - legend_border_size: Border width of the legend box.
    - legend_text_color: Color of the legend text.

    Returns:
    - A configured LegendOpts object.
    """
    if legend == 'right':
        return opts.LegendOpts(
            pos_right=legend_pos_right,
            pos_top=legend_pos_top,
            orient="vertical",
            border_width=legend_border_size,
            textstyle_opts=opts.TextStyleOpts(color=legend_text_color),
        )
    elif legend == 'top':
        return opts.LegendOpts(
            pos_top=legend_pos_top,
            border_width=legend_border_size,
            textstyle_opts=opts.TextStyleOpts(color=legend_text_color),
        )
    else:
        return opts.LegendOpts(is_show=False)


def configure_global_chart_options(
    global_options,
    axis_pointer_type="line",
    brush=False,
    data_zoom=False,
    toolbox=False,
):
    """
    Configure common global chart options like tooltip, brush, data zoom, and toolbox.

    Parameters:
    - global_options: The existing GlobalOptions dictionary to update.
    - axis_pointer_type: The type of axis pointer for the tooltip (default: "line").
    - brush: Whether to include brush options (default: False).
    - data_zoom: Whether to include data zoom options (default: False).
    - toolbox: Whether to include toolbox options (default: False).

    Returns:
    - The updated GlobalOptions dictionary.
    """
    # Add or update tooltip options
    global_options["tooltip_opts"] = opts.TooltipOpts(trigger="axis", axis_pointer_type=axis_pointer_type)

    # Add brush options if enabled
    if brush:
        global_options["brush_opts"] = opts.BrushOpts()

    # Add data zoom options if enabled
    if data_zoom:
        global_options["datazoom_opts"] = get_datazoom_options()

    # Add toolbox options if enabled
    if toolbox:
        global_options["toolbox_opts"] = get_toolbox_options()

    return global_options


def configure_marklines(
    chart,
    horizontal_line=None,
    horizontal_line_name=None,
    vertical_line=None,
    vertical_line_name=None,
):
    """
    Configure a chart with global options and add horizontal/vertical marklines.

    Parameters:
    - chart: The chart object to update.
    - horizontal_line: The Y-coordinate for the horizontal markline (default: None).
    - horizontal_line_name: The name/label for the horizontal markline (default: None).
    - vertical_line: The X-coordinate for the vertical markline (default: None).
    - vertical_line_name: The name/label for the vertical markline (default: None).

    Returns:
    - The updated chart object.
    """
    # Add marklines if specified
    if horizontal_line is not None or vertical_line is not None:
        markline_data = []

        if horizontal_line is not None:
            markline_data.append(opts.MarkLineItem(y=horizontal_line, name=horizontal_line_name))

        if vertical_line is not None:
            markline_data.append(opts.MarkLineItem(x=vertical_line, name=vertical_line_name))

        chart = chart.set_series_opts(markline_opts=opts.MarkLineOpts(data=markline_data))

    return chart


#################################################################################################


def Histogram(dt = None,
              SampleSize = None,
              YVar = None,
              YVarTrans = None,
              GroupVar = None,
              FacetRows = 1,
              FacetCols = 1,
              FacetLevels = None,
              TimeLine = False,
              NumberBins = 20,
              RenderHTML = None,
              CategoryGap = "10%",
              Theme = 'wonderland',
              BackgroundColor = None,
              Width = None,
              Height = None,
              ToolBox = True,
              Brush = True,
              DataZoom = True,
              Title = 'Histogram',
              TitleColor = "#fff",
              TitleFontSize = 20,
              SubTitle = None,
              SubTitleColor = "#fff",
              SubTitleFontSize = 12,
              AxisPointerType = 'cross',
              XAxisTitle = None,
              XAxisNameLocation = 'middle',
              XAxisNameGap = 42,
              Legend = None,
              LegendPosRight = '0%',
              LegendPosTop = '5%',
              LegendBorderSize = 0.25,
              LegendTextColor = "#fff",
              VerticalLine = None,
              VerticalLineName = 'Line Name',
              HorizontalLine = None,
              HorizontalLineName = 'Line Name',
              AnimationThreshold = 2000,
              AnimationDuration = 1000,
              AnimationEasing = "cubicOut",
              AnimationDelay = 0,
              AnimationDurationUpdate = 300,
              AnimationEasingUpdate = "cubicOut",
              AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    NumberBins: number of histogram bins. Default is 20
    CategoryGap: amount of spacing between bars
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot. The number here is based on the number bucket of the histogram
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """

    # Set to YVar if not None
    if XAxisTitle == None:
      XAxisTitle = YVar

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    if GroupVar == None:
      dt1 = dt1.select([pl.col(YVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Single Histogram, no grouping
    if GroupVar == None:
      Min = dt1.select(pl.min(YVar))
      Max = dt1.select(pl.max(YVar))
      Range = (Max - Min).to_series()[0]
      if Range < NumberBins:
        acc = round(Range / NumberBins, ndigits = 2)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.len().alias(YVar))
        dt1 = dt1.sort("Buckets")
      else:
        acc = math.ceil(Range / NumberBins)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.len().alias(YVar))
        dt1 = dt1.sort("Buckets")

      # Define data elements
      Buckets = dt1['Buckets'].to_list()
      YVal = dt1[YVar].to_list()
      
      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      c = PyBar(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(Buckets)
      c = c.add_yaxis(YVar, YVal, stack = "stack1", category_gap = CategoryGap)

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Group Variable Case
    else:

      # Time utilizes all levels; Facet only uses enough to fill grid
      if not TimeLine:
        if not FacetLevels is None:
          levs = FacetLevels
        else:
          levs = dt1[GroupVar].unique().sort()[0:(FacetCols * FacetRows)]
      else:
        levs = dt1[GroupVar].unique().sort()

      # Build individual plots
      plot_dict = {}
      for i in levs: # i = levs[0]
        GlobalOptions = {}
        dt2 = dt1.filter(dt1[GroupVar] == i)
        Min = dt2.select(pl.min(YVar))
        Max = dt2.select(pl.max(YVar))
        Range = (Max - Min).to_series()[0]
        if Range < NumberBins:
          acc = round(Range / NumberBins, ndigits = 2)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.len().alias(YVar))
          dt2 = dt2.sort("Buckets")
        else:
          acc = math.ceil(Range / NumberBins)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.len().alias(YVar))
          dt2 = dt2.sort("Buckets")

        # Define data elements
        Buckets = dt2['Buckets'].to_list().copy()
        YVal = dt2[YVar].to_list().copy()
        
        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)
  
        # Create plot
        plot_dict[i] = PyBar(init_opts = opts.InitOpts(**InitOptions))
        plot_dict[i] = plot_dict[i].add_xaxis(Buckets)
        plot_dict[i] = plot_dict[i].add_yaxis(YVar, YVal, stack = "stack1", category_gap = CategoryGap)

        # Global Options
        GlobalOptions = {}
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
    
        # Series Options
        plot_dict[i] = configure_marklines(
          chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

    # Facet Output
    if not TimeLine:
      
      # Setup Grid Output
      facet_vals = FacetGridValues(
        FacetRows = FacetRows,
        FacetCols = FacetCols,
        Legend = Legend,
        LegendSpace = 10,
        Width = Width,
        Height = Height)
      if not Width:
        Width = "1250px"
      if not Height:
        Height = "750px"
      grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
      counter = -1
      for i in levs:
        counter += 1
        grid = grid.add(
          plot_dict[i],
          grid_opts = opts.GridOpts(
            pos_left = f"{facet_vals['left'][counter]}%",
            pos_top = f"{facet_vals['top'][counter]}%",
            width = f"{facet_vals['Width_f']}%",
            height = f"{facet_vals['Height_f']}%"))

      # Render html
      if RenderHTML:
        grid.render(f"{RenderHTML}.html")

      return grid

    # TimeLine Output
    else:

      tl = Timeline()
      for i in levs:
        tl.add(plot_dict[i], i)

      # Render html
      if RenderHTML:
        tl.render(f"{RenderHTML}.html")

      return tl


#################################################################################################


def Density(dt = None,
            SampleSize = None,
            YVar = None,
            GroupVar = None,
            FacetRows = 1,
            FacetCols = 1,
            FacetLevels = None,
            TimeLine = False,
            YVarTrans = None,
            RenderHTML = None,
            LineWidth = 2,
            FillOpacity = 0.5,
            Theme = 'wonderland',
            BackgroundColor = None,
            Width = None,
            Height = None,
            ToolBox = True,
            Brush = True,
            DataZoom = True,
            Title = 'Density Plot',
            TitleColor = "#fff",
            TitleFontSize = 20,
            SubTitle = None,
            SubTitleColor = "#fff",
            SubTitleFontSize = 12,
            AxisPointerType = 'cross',
            XAxisTitle = None,
            XAxisNameLocation = 'middle',
            XAxisNameGap = 42,
            Legend = None,
            LegendPosRight = '0%',
            LegendPosTop = '5%',
            LegendBorderSize = 0.25,
            LegendTextColor = "#fff",
            VerticalLine = None,
            VerticalLineName = 'Line Name',
            HorizontalLine = None,
            HorizontalLineName = 'Line Name',
            AnimationThreshold = 2000,
            AnimationDuration = 1000,
            AnimationEasing = "cubicOut",
            AnimationDelay = 0,
            AnimationDurationUpdate = 300,
            AnimationEasingUpdate = "cubicOut",
            AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    LineWidth: numeric. Default is 2
    FillOpacity: fill opacity under the line. Default 0.5
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """

    NumberBins = 20
    
    if XAxisTitle == None:
      XAxisTitle = YVar

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    if GroupVar == None:
      dt1 = dt1.select([pl.col(YVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Single Histogram, no grouping
    if GroupVar == None:
      Min = dt1.select(pl.min(YVar))
      Max = dt1.select(pl.max(YVar))
      Range = (Max - Min).to_series()[0]
      if Range < NumberBins:
        acc = round(Range / NumberBins, ndigits = 2)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.len().alias(YVar))
        dt1 = dt1.sort("Buckets")
      else:
        acc = math.ceil(Range / NumberBins)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.len().alias(YVar))
        dt1 = dt1.sort("Buckets")

      # Define data elements
      Buckets = dt1['Buckets'].to_list()
      Buckets = [str(b) for b in Buckets]
      YVal = dt1[YVar].to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(Buckets)
      c = c.add_yaxis(
        YVar,
        YVal,
        is_smooth = True,
        linestyle_opts = opts.LineStyleOpts(width = LineWidth),
        areastyle_opts = opts.AreaStyleOpts(opacity = FillOpacity))

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Group Variable Case
    else:
      
      # Time utilizes all levels; Facet only uses enough to fill grid
      if not TimeLine:
        if not FacetLevels is None:
          levs = FacetLevels
        else:
          levs = dt1[GroupVar].unique().sort()[0:(FacetCols * FacetRows)]
      else:
        levs = dt1[GroupVar].unique().sort()

      plot_dict = {}
      for i in levs: # i = levs[0]
        GlobalOptions = {}
        dt2 = dt1.filter(dt1[GroupVar] == i)
        Min = dt2.select(pl.min(YVar))
        Max = dt2.select(pl.max(YVar))
        Range = (Max - Min).to_series()[0]
        if Range < NumberBins:
          acc = round(Range / NumberBins, ndigits = 2)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.len().alias(YVar))
          dt2 = dt2.sort("Buckets")
        else:
          acc = math.ceil(Range / NumberBins)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.len().alias(YVar))
          dt2 = dt2.sort("Buckets")
       
        # Define data elements
        Buckets = dt2['Buckets'].to_list().copy()
        YVal = dt2[YVar].to_list().copy()
        
        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)
       
        # Create plot
        plot_dict[i] = PyLine(init_opts = opts.InitOpts(theme = Theme))
        plot_dict[i] = plot_dict[i].add_xaxis(Buckets)
        plot_dict[i] = plot_dict[i].add_yaxis(
          YVar,
          YVal,
          is_smooth = True,
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          areastyle_opts = opts.AreaStyleOpts(opacity = FillOpacity))
        
        # Global Options
        GlobalOptions = {}
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
    
        # Series Options
        plot_dict[i] = configure_marklines(
          chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

    # Facet Output
    if not TimeLine:

      # Setup Grid Output
      facet_vals = FacetGridValues(
        FacetRows = FacetRows,
        FacetCols = FacetCols,
        Legend = Legend,
        LegendSpace = 10,
        Width = Width,
        Height = Height)
      if not Width:
        Width = "1250px"
      if not Height:
        Height = "750px"
      grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
      counter = -1
      for i in levs:
        counter += 1
        grid = grid.add(
          plot_dict[i],
          grid_opts = opts.GridOpts(
            pos_left = f"{facet_vals['left'][counter]}%",
            pos_top = f"{facet_vals['top'][counter]}%",
            width = f"{facet_vals['Width_f']}%",
            height = f"{facet_vals['Height_f']}%"))
  
      # Render html
      if RenderHTML:
        grid.render(f"{RenderHTML}.html")
    
      return grid
  
    # TimeLine Output
    else:

      tl = Timeline()
      for i in levs:
        tl.add(plot_dict[i], i)

      # Render html
      if RenderHTML:
        tl.render(f"{RenderHTML}.html")

      return tl


#################################################################################################


def Pie(dt = None,
        PreAgg = False,
        YVar = None,
        GroupVar = None,
        AggMethod = 'count',
        YVarTrans = None,
        RenderHTML = None,
        Theme = 'wonderland',
        BackgroundColor = None,
        Width = None,
        Height = None,
        Title = 'Pie Chart',
        TitleColor = "#fff",
        TitleFontSize = 20,
        SubTitle = None,
        SubTitleColor = "#fff",
        SubTitleFontSize = 12,
        Legend = None,
        LegendPosRight = '0%',
        LegendPosTop = '5%',
        LegendBorderSize = 0.25,
        LegendTextColor = "#fff",
        AnimationThreshold = 2000,
        AnimationDuration = 1000,
        AnimationEasing = "cubicOut",
        AnimationDelay = 0,
        AnimationDurationUpdate = 300,
        AnimationEasingUpdate = "cubicOut",
        AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """


    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = None)

    # Define data elements
    GroupVals = dt1[GroupVar].to_list()
    YVal = dt1[YVar].to_list()
    data_pair = [list(z) for z in zip(GroupVals, YVal)]
    data_pair.sort(key=lambda x: x[1])

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyPie(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
        series_name = YVar,
        data_pair = data_pair,
        center = ["50%", "50%"],
        label_opts = opts.LabelOpts(is_show = False, position = "center"),
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    c = c.set_series_opts(
      tooltip_opts = opts.TooltipOpts(
        trigger = "item", 
        formatter="{a} <br/>{b}: {c} ({d}%)"
      ),
      label_opts = opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    
    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def Rosetype(dt = None,
             PreAgg = False,
             YVar = None,
             GroupVar = None,
             AggMethod = 'count',
             YVarTrans = None,
             RenderHTML = None,
             Type = "radius",
             Radius = "55%",
             Theme = 'wonderland',
             BackgroundColor = None,
             Width = None,
             Height = None,
             Title = 'Rosetype Chart',
             TitleColor = "#fff",
             TitleFontSize = 20,
             SubTitle = None,
             SubTitleColor = "#fff",
             SubTitleFontSize = 12,
             Legend = None,
             LegendPosRight = '0%',
             LegendPosTop = '5%',
             LegendBorderSize = 0.25,
             LegendTextColor = "#fff",
             AnimationThreshold = 2000,
             AnimationDuration = 1000,
             AnimationEasing = "cubicOut",
             AnimationDelay = 0,
             AnimationDurationUpdate = 300,
             AnimationEasingUpdate = "cubicOut",
             AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Type: Default "radius". Otherwise, "area"
    Radius: Default "55%"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = None)

    # Define data elements
    GroupVals = dt1[GroupVar].to_list()
    YVal = dt1[YVar].to_list()
    data_pair = [list(z) for z in zip(GroupVals, YVal)]
    data_pair.sort(key=lambda x: x[1])

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyPie(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
        series_name = YVar,
        data_pair = data_pair,
        rosetype = Type,
        radius = Radius,
        center = ["50%", "50%"],
        label_opts = opts.LabelOpts(is_show=False, position="center"),
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    c = c.set_series_opts(
      tooltip_opts = opts.TooltipOpts(
        trigger = "item", 
        formatter="{a} <br/>{b}: {c} ({d}%)"
      ),
      label_opts = opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    
    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def Donut(dt = None,
          PreAgg = False,
          YVar = None,
          GroupVar = None,
          AggMethod = 'count',
          YVarTrans = None,
          RenderHTML = None,
          Theme = 'wonderland',
          BackgroundColor = None,
          Width = None,
          Height = None,
          Title = 'Donut Chart',
          TitleColor = "#fff",
          TitleFontSize = 20,
          SubTitle = None,
          SubTitleColor = "#fff",
          SubTitleFontSize = 12,
          Legend = None,
          LegendPosRight = '0%',
          LegendPosTop = '5%',
          LegendBorderSize = 0.25,
          LegendTextColor = "#fff",
          AnimationThreshold = 2000,
          AnimationDuration = 1000,
          AnimationEasing = "cubicOut",
          AnimationDelay = 0,
          AnimationDurationUpdate = 300,
          AnimationEasingUpdate = "cubicOut",
          AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = None)

    # Define data elements
    GroupVals = dt1[GroupVar].to_list()
    YVal = dt1[YVar].to_list()
    data_pair = [list(z) for z in zip(GroupVals, YVal)]
    data_pair.sort(key=lambda x: x[1])
    
    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyPie(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
      series_name = YVar,
      data_pair = data_pair,
      radius = ["40%","70%"],
      center = ["50%", "50%"],
      label_opts = opts.LabelOpts(is_show=False, position="center"),
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    c = c.set_series_opts(
      tooltip_opts = opts.TooltipOpts(
        trigger = "item", 
        formatter="{a} <br/>{b}: {c} ({d}%)"
      ),
      label_opts = opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    
    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c

#################################################################################################


def BoxPlot(dt = None,
            SampleSize = None,
            YVar = None,
            GroupVar = None,
            YVarTrans = None,
            RenderHTML = None,
            Theme = 'wonderland',
            BackgroundColor = None,
            Width = None,
            Height = None,
            ToolBox = True,
            Brush = True,
            DataZoom = True,
            Title = 'Box Plot',
            TitleColor = "#fff",
            TitleFontSize = 20,
            SubTitle = None,
            SubTitleColor = "#fff",
            SubTitleFontSize = 12,
            AxisPointerType = 'cross',
            YAxisTitle = None,
            YAxisNameLocation = 'middle',
            YAxisNameGap = 42,
            XAxisTitle = None,
            XAxisNameLocation = 'middle',
            XAxisNameGap = 42,
            Legend = None,
            LegendPosRight = '0%',
            LegendPosTop = '5%',
            LegendBorderSize = 0.25,
            LegendTextColor = "#fff",
            HorizontalLine = None,
            HorizontalLineName = 'Line Name',
            AnimationThreshold = 2000,
            AnimationDuration = 1000,
            AnimationEasing = "cubicOut",
            AnimationDelay = 0,
            AnimationDurationUpdate = 300,
            AnimationEasingUpdate = "cubicOut",
            AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable
    GroupVar: grouping variable
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    if XAxisTitle == None and not GroupVar is None:
      XAxisTitle = GroupVar

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Define Plotting Variable
    if YVar == None:
      return None
    # YVar and GroupVar Mgt
    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if GroupVar == None:
      dt1 = dt1.select([pl.col(YVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 1
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = Boxplot(init_opts = opts.InitOpts(**InitOptions))
    if not GroupVar is None:
      Buckets = dt1[GroupVar].unique().to_list()
      Buckets.sort()
      bucket_data = []
      c = c.add_xaxis(Buckets)
      for i in Buckets: # i = 'Angel'
        bucket_data.append(dt1.filter(dt1[GroupVar] == i)[YVar].to_list())
      c = c.add_yaxis('YVar', c.prepare_data(bucket_data))
    else:
      if isinstance(YVar, list):
        c = c.add_xaxis(YVar)
        bucket_data = []
        for yvar in YVar:
          bucket_data.append(dt1[yvar].to_list())

        c = c.add_yaxis('YVar', c.prepare_data(bucket_data))
      else:
        YVal = [dt1[YVar].to_list()]
        c = c.add_yaxis(YVar, c.prepare_data(YVal))

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
      
    GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
    GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
    GlobalOptions = configure_global_chart_options(
      global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
      brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
    
    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Series Options
    if not HorizontalLine is None:
      MarkLineDict = {}
      MarkLineDict['data'] = [opts.MarkLineItem(y = HorizontalLine, name = HorizontalLineName)]
      c = c.set_series_opts(markline_opts = opts.MarkLineOpts(**MarkLineDict))

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def WordCloud(dt = None,
              SampleSize = None,
              YVar = None,
              RenderHTML = None,
              Title = 'Word Cloud',
              TitleColor = "#fff",
              TitleFontSize = 20,
              SubTitle = None,
              SubTitleColor = "#fff",
              SubTitleFontSize = 12,
              Theme = 'wonderland',
              BackgroundColor = None,
              Width = None,
              Height = None,
              AnimationThreshold = 2000,
              AnimationDuration = 1000,
              AnimationEasing = "cubicOut",
              AnimationDelay = 0,
              AnimationDurationUpdate = 300,
              AnimationEasingUpdate = "cubicOut",
              AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    dt1 = dt1.select([pl.col(YVar)])
    
    # Define data elements
    dt1 = dt1.group_by(pl.col(YVar)).agg(pl.count(YVar).alias('Count'))
    GroupVals = dt1[YVar]
    YVal = dt1['Count']
    data_pair = [list(z) for z in zip(GroupVals, YVal)]
    data_pair.sort(key=lambda x: x[1])

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyWordCloud(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(series_name = YVar, data_pair = data_pair)

    # Global Options
    GlobalOptions = {}
    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def Radar(dt = None,
          YVar = None,
          GroupVar = None,
          AggMethod = 'mean',
          YVarTrans = None,
          RenderHTML = None,
          LabelColor = '#fff',
          LineColors = ["#213f7f", "#00a6fb", "#22c0df", "#8e5fa8", "#ed1690"],
          Theme = 'wonderland',
          BackgroundColor = None,
          Width = None,
          Height = None,
          Title = 'Radar Chart',
          TitleColor = "#fff",
          TitleFontSize = 20,
          SubTitle = None,
          SubTitleColor = "#fff",
          SubTitleFontSize = 12,
          Legend = None,
          LegendPosRight = '0%',
          LegendPosTop = '5%',
          LegendBorderSize = 0.25,
          LegendTextColor = "#fff",
          AnimationThreshold = 2000,
          AnimationDuration = 1000,
          AnimationEasing = "cubicOut",
          AnimationDelay = 0,
          AnimationDurationUpdate = 300,
          AnimationEasingUpdate = "cubicOut",
          AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    LabelColor: color for the radar category labels. Default is '#fff'
    LineColors: Default list ["#213f7f", "#00a6fb", "#22c0df", "#8e5fa8", "#ed1690"]. If you need more add more.
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())

    # Define data elements
    vals_dict = {}
    if not isinstance(YVar, list):
      yVar = [YVar]
    else:
      yVar = YVar
    counter = -1
    for yvar in yVar:# yvar = yVar
      counter += 1
      temp = PolarsAggregation(dt1, AggMethod, NumericVariable = yvar, GroupVariable = GroupVar, DateVariable = None) 
      vals_dict[yvar] = [round(num, 2) for num in temp[yvar]]

    group_levels = dt1[GroupVar].unique()

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyRadar(init_opts = opts.InitOpts(**InitOptions))
    schema = []
    for gv in group_levels:
      schema.append(opts.RadarIndicatorItem(name = gv))

    c = c.add_schema(
      schema = schema,
      splitarea_opt = opts.SplitAreaOpts(is_show = True, areastyle_opts = opts.AreaStyleOpts(opacity = 1)),
      textstyle_opts = opts.TextStyleOpts(color = LabelColor),
    )

    vals_dict_keys = list(vals_dict.keys())
    counter = -1
    for i in vals_dict_keys: # i = vals_dict_keys[0]
      counter += 1
      c = c.add(
        series_name = vals_dict_keys[counter],
        data = [vals_dict[i]],
        linestyle_opts = opts.LineStyleOpts(color = LineColors[counter]),
      )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c


#################################################################################################


def Line(dt = None,
         PreAgg = False,
         YVar = None,
         XVar = None,
         GroupVar = None,
         AggMethod = 'mean',
         FacetRows = 1,
         FacetCols = 1,
         FacetLevels = None,
         TimeLine = False,
         YVarTrans = None,
         RenderHTML = None,
         SmoothLine = True,
         LineWidth = 2,
         Symbol = "emptyCircle",
         SymbolSize = 6,
         ShowLabels = False,
         LabelPosition = "top",
         Theme = 'wonderland',
         BackgroundColor = None,
         Width = None,
         Height = None,
         ToolBox = True,
         Brush = True,
         DataZoom = True,
         Title = 'Line Plot',
         TitleColor = "#fff",
         TitleFontSize = 20,
         SubTitle = None,
         SubTitleColor = "#fff",
         SubTitleFontSize = 12,
         AxisPointerType = 'cross',
         YAxisTitle = None,
         YAxisNameLocation = 'middle',
         YAxisNameGap = 70,
         XAxisTitle = None,
         XAxisNameLocation = 'middle',
         XAxisNameGap = 42,
         Legend = None,
         LegendPosRight = '0%',
         LegendPosTop = '5%',
         LegendBorderSize = 0.25,
         LegendTextColor = "#fff",
         VerticalLine = None,
         VerticalLineName = 'Line Name',
         HorizontalLine = None,
         HorizontalLineName = 'Line Name',
         AnimationThreshold = 2000,
         AnimationDuration = 1000,
         AnimationEasing = "cubicOut",
         AnimationDelay = 0,
         AnimationDurationUpdate = 300,
         AnimationEasingUpdate = "cubicOut",
         AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    SmoothLine: Logical
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None
        
    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())

    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        c = c.add_yaxis(
          series_name = yvar,
          is_smooth = SmoothLine,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyLine(init_opts = opts.InitOpts(**InitOptions))
        c = c.add_xaxis(xaxis_data = XVal)
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for yvar in GroupLevels:# yvar_dict.keys()
          c = c.add_yaxis(
            series_name = yvar,
            is_smooth = SmoothLine,
            symbol = Symbol,
            symbol_size = SymbolSize,
            is_symbol_show = ShowSymbol,
            y_axis = yvar_dict[yvar],
            linestyle_opts = opts.LineStyleOpts(width = LineWidth),
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )
  
        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        if not Title is None:
          GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        yvar_dict = {}
        plot_dict = {}

        # Time utilizes all levels; Facet only uses enough to fill grid
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()
        
        # Create plot
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for i in GroupLevels:# i = 'Yellow-Yum'
          # Create plot
          InitOptions = initialize_options(
            theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
            animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
            animation_easing=AnimationEasing, animation_delay=AnimationDelay,
            animation_duration_update=AnimationDurationUpdate, 
            animation_easing_update=AnimationEasingUpdate,
            animation_delay_update=AnimationDelayUpdate)

          plot_dict[i] = PyLine(init_opts = opts.InitOpts(**InitOptions))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = XVal)
          plot_dict[i] = plot_dict[i].add_yaxis(
            series_name = i,
            is_smooth = SmoothLine,
            symbol = Symbol,
            symbol_size = SymbolSize,
            is_symbol_show = ShowSymbol,
            y_axis = yvar_dict[i],
            linestyle_opts = opts.LineStyleOpts(width = LineWidth),
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

          # Global Options
          GlobalOptions = {}
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
          GlobalOptions = configure_global_chart_options(
            global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
            brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
    
          # Final Setting of Global Options
          plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
      
          # Series Options
          plot_dict[i] = configure_marklines(
            chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
            vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

        if not TimeLine:

          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))
  
          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:
          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)

          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")
    
          return tl


#################################################################################################


def StackedLine(dt = None,
                PreAgg = False,
                YVar = None,
                XVar = None,
                GroupVar = None,
                AggMethod = 'mean',
                YVarTrans = None,
                RenderHTML = None,
                SmoothLine = True,
                LineWidth = 2,
                Symbol = "emptyCircle",
                SymbolSize = 6,
                ShowLabels = False,
                LabelPosition = "top",
                Theme = 'wonderland',
                BackgroundColor = None,
                Width = None,
                Height = None,
                ToolBox = True,
                Brush = True,
                DataZoom = True,
                Title = 'Stacked Line',
                TitleColor = "#fff",
                TitleFontSize = 20,
                SubTitle = None,
                SubTitleColor = "#fff",
                SubTitleFontSize = 12,
                AxisPointerType = 'cross',
                YAxisTitle = None,
                YAxisNameLocation = 'middle',
                YAxisNameGap = 70,
                XAxisTitle = None,
                XAxisNameLocation = 'middle',
                XAxisNameGap = 42,
                Legend = None,
                LegendPosRight = '0%',
                LegendPosTop = '5%',
                LegendBorderSize = 0.25,
                LegendTextColor = "#fff",
                AnimationThreshold = 2000,
                AnimationDuration = 1000,
                AnimationEasing = "cubicOut",
                AnimationDelay = 0,
                AnimationDurationUpdate = 300,
                AnimationEasingUpdate = "cubicOut",
                AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    SmoothLine: Logical
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if not isinstance(YVar, list) and GroupVar is None:
      return None
    else:
      if len(YVar) == 1 and GroupVar is None:
        return None

    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          is_smooth = SmoothLine,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:
        
      yvar_dict = {}
      GroupLevels = dt1[GroupVar].unique().sort().to_list()
      for gv in GroupLevels:
        temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
        yvar_dict[gv] = temp[YVar].to_list()

      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in GroupLevels:# yvar_dict.keys()
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          is_smooth = SmoothLine,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c


#################################################################################################


def Step(dt = None,
         PreAgg = False,
         YVar = None,
         XVar = None,
         GroupVar = None,
         FacetRows = 1,
         FacetCols = 1,
         FacetLevels = None,
         TimeLine = False,
         AggMethod = 'mean',
         YVarTrans = None,
         RenderHTML = None,
         LineWidth = 2,
         Symbol = "emptyCircle",
         SymbolSize = 6,
         ShowLabels = False,
         LabelPosition = "top",
         Theme = 'wonderland',
         BackgroundColor = None,
         Height = None,
         Width = None,
         ToolBox = True,
         Brush = True,
         DataZoom = True,
         Title = 'Line Plot',
         TitleColor = "#fff",
         TitleFontSize = 20,
         SubTitle = None,
         SubTitleColor = "#fff",
         SubTitleFontSize = 12,
         AxisPointerType = 'cross',
         YAxisTitle = None,
         YAxisNameLocation = 'middle',
         YAxisNameGap = 70,
         XAxisTitle = None,
         XAxisNameLocation = 'middle',
         XAxisNameGap = 42,
         Legend = None,
         LegendPosRight = '0%',
         LegendPosTop = '5%',
         LegendBorderSize = 0.25,
         LegendTextColor = "#fff",
         VerticalLine = None,
         VerticalLineName = 'Line Name',
         HorizontalLine = None,
         HorizontalLineName = 'Line Name',
         AnimationThreshold = 2000,
         AnimationDuration = 1000,
         AnimationEasing = "cubicOut",
         AnimationDelay = 0,
         AnimationDurationUpdate = 300,
         AnimationEasingUpdate = "cubicOut",
         AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        c = c.add_yaxis(
          series_name = yvar,
          is_step = True,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()
  
        XVal = dt1[XVar].unique().to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyLine(init_opts = opts.InitOpts(**InitOptions))
        c = c.add_xaxis(xaxis_data = XVal)
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for yvar in yvar_dict.keys():# yvar_dict.keys()
          c = c.add_yaxis(
            series_name = yvar,
            is_step = True,
            symbol = Symbol,
            symbol_size = SymbolSize,
            is_symbol_show = ShowSymbol,
            y_axis = yvar_dict[yvar],
            linestyle_opts = opts.LineStyleOpts(width = LineWidth),
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )
  
        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        if not Title is None:
          GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        yvar_dict = {}
        plot_dict = {}

        # Time utilizes all levels; Facet only uses enough to fill grid
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()
        
        # Create plot
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for i in GroupLevels:# i = 'Yellow-Yum'
          
          # Create plot
          InitOptions = initialize_options(
            theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
            animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
            animation_easing=AnimationEasing, animation_delay=AnimationDelay,
            animation_duration_update=AnimationDurationUpdate, 
            animation_easing_update=AnimationEasingUpdate,
            animation_delay_update=AnimationDelayUpdate)
          
          plot_dict[i] = PyLine(init_opts = opts.InitOpts(**InitOptions))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = XVal)
          plot_dict[i] = plot_dict[i].add_yaxis(
            series_name = i,
            is_step = True,
            symbol = Symbol,
            symbol_size = SymbolSize,
            is_symbol_show = ShowSymbol,
            y_axis = yvar_dict[i],
            linestyle_opts = opts.LineStyleOpts(width = LineWidth),
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

          # Global Options
          # Global Options
        GlobalOptions = {}
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
    
        # Series Options
        plot_dict[i] = configure_marklines(
          chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

        # Facet Output
        if not TimeLine:
          
          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))
  
          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:
          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)

          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")
    
          return tl


#################################################################################################


def StackedStep(dt = None,
                PreAgg = False,
                YVar = None,
                XVar = None,
                GroupVar = None,
                AggMethod = 'mean',
                YVarTrans = None,
                RenderHTML = None,
                LineWidth = 2,
                Symbol = "emptyCircle",
                SymbolSize = 6,
                ShowLabels = False,
                LabelPosition = "top",
                Theme = 'wonderland',
                BackgroundColor = None,
                Width = None,
                Height = None,
                ToolBox = True,
                Brush = True,
                DataZoom = True,
                Title = 'Line Plot',
                TitleColor = "#fff",
                TitleFontSize = 20,
                SubTitle = None,
                SubTitleColor = "#fff",
                SubTitleFontSize = 12,
                AxisPointerType = 'cross',
                YAxisTitle = None,
                YAxisNameLocation = 'middle',
                YAxisNameGap = 70,
                XAxisTitle = None,
                XAxisNameLocation = 'middle',
                XAxisNameGap = 42,
                Legend = None,
                LegendPosRight = '0%',
                LegendPosTop = '5%',
                LegendBorderSize = 0.25,
                LegendTextColor = "#fff",
                AnimationThreshold = 2000,
                AnimationDuration = 1000,
                AnimationEasing = "cubicOut",
                AnimationDelay = 0,
                AnimationDurationUpdate = 300,
                AnimationEasingUpdate = "cubicOut",
                AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if not isinstance(YVar, list) and GroupVar is None:
      return None
    else:
      if len(YVar) == 1 and GroupVar is None:
        return None

    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          is_step = True,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      yvar_dict = {}
      GroupLevels = dt1[GroupVar].unique().sort().to_list()
      for gv in GroupLevels:
        temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
        yvar_dict[gv] = temp[YVar].to_list()

      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in yvar_dict.keys():# yvar_dict.keys()
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          is_step = True,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c


#################################################################################################

def JS_GradientAreaBackground(Color1, Color2):
    background_color_js = (
        f"new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        f"[{{offset: 0, color: '{Color1}'}}, {{offset: 1, color: '{Color2}'}}], false)"
    )
    return background_color_js

# JS_GradientAreaBackground('#c86589', '#06a7ff')

def JS_GradientAreaFill(gradient_colors):
    """
    Generate JavaScript code for an ECharts gradient area fill.

    Parameters:
    - gradient_colors: A list or tuple containing one or more color strings.

    Returns:
    - A string of JavaScript code for the gradient area fill.
    """
    if not gradient_colors or len(gradient_colors) < 1:
        raise ValueError("gradient_colors must contain at least one color.")

    stops = []
    step = 1 / (len(gradient_colors) - 1) if len(gradient_colors) > 1 else 0

    for i, color in enumerate(gradient_colors):
        stops.append(f"{{offset: {i * step:.2f}, color: '{color}'}}")

    area_color_js = f"new echarts.graphic.LinearGradient(0, 0, 0, 1, [{', '.join(stops)}], false)"
    return area_color_js

#################################################################################################


def Area(dt = None,
         PreAgg = False,
         YVar = None,
         XVar = None,
         GroupVar = None,
         FacetRows = 1,
         FacetCols = 1,
         FacetLevels = None,
         TimeLine = False,
         AggMethod = 'mean',
         YVarTrans = None,
         RenderHTML = None,
         Opacity = 0.5,
         GradientColors = ['#c86589', '#06a7ff0d'],
         LineWidth = 2,
         Symbol = "emptyCircle",
         SymbolSize = 6,
         ShowLabels = False,
         LabelPosition = "top",
         Theme = 'wonderland',
         BackgroundColor = None,
         Width = None,
         Height = None,
         ToolBox = True,
         Brush = True,
         DataZoom = True,
         Title = 'Area Plot',
         TitleColor = "#fff",
         TitleFontSize = 20,
         SubTitle = None,
         SubTitleColor = "#fff",
         SubTitleFontSize = 12,
         AxisPointerType = 'cross',
         YAxisTitle = None,
         YAxisNameLocation = 'middle',
         YAxisNameGap = 70,
         XAxisTitle = None,
         XAxisNameLocation = 'middle',
         XAxisNameGap = 42,
         Legend = None,
         LegendPosRight = '0%',
         LegendPosTop = '5%',
         LegendBorderSize = 0.25,
         LegendTextColor = "#fff",
         VerticalLine = None,
         VerticalLineName = 'Line Name',
         HorizontalLine = None,
         HorizontalLineName = 'Line Name',
         AnimationThreshold = 2000,
         AnimationDuration = 1000,
         AnimationEasing = "cubicOut",
         AnimationDelay = 0,
         AnimationDurationUpdate = 300,
         AnimationEasingUpdate = "cubicOut",
         AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Opacity: For grouping plots. Defaults to 0.5
    GradientColors: list of hex colors
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    
    # Ensure GradientColors is in a list
    if not isinstance(GradientColors, list):
      GradientColors = list(GradientColors)

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())


    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    # No GroupVar
    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        yaxis_options = {}
        yaxis_options['series_name'] = yvar
        yaxis_options['is_smooth'] = True
        yaxis_options['symbol'] = Symbol
        yaxis_options['symbol_size'] = SymbolSize,
        yaxis_options['is_symbol_show'] = ShowSymbol
        yaxis_options['y_axis'] = yvar_dict[yvar]
        yaxis_options['linestyle_opts'] = opts.LineStyleOpts(width = LineWidth)
        yaxis_options['label_opts'] = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition)
        if isinstance(YVar, list):
          if len(YVar) == 1:
            yaxis_options['areastyle_opts'] = opts.AreaStyleOpts(color = JsCode(JS_GradientAreaFill(GradientColors)), opacity=Opacity)
          else:
            yaxis_options['areastyle_opts'] = opts.AreaStyleOpts(opacity = Opacity)
        else:
          yaxis_options['areastyle_opts'] = opts.AreaStyleOpts(color = JsCode(JS_GradientAreaFill(GradientColors)), opacity=Opacity)

        c = c.add_yaxis(**yaxis_options)

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()
  
        XVal = dt1[XVar].unique().to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyLine(init_opts = opts.InitOpts(**InitOptions))
        c = c.add_xaxis(xaxis_data = XVal)
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for yvar in GroupLevels:
          c = c.add_yaxis(
            series_name = yvar,
            symbol = Symbol,
            symbol_size = SymbolSize,
            is_smooth = True,
            is_symbol_show = ShowSymbol,
            y_axis = yvar_dict[yvar],
            areastyle_opts = opts.AreaStyleOpts(opacity = Opacity),
            linestyle_opts = opts.LineStyleOpts(width = LineWidth),
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )
          
        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        if not Title is None:
          GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        yvar_dict = {}
        plot_dict = {}
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()

        # Create plot
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for i in GroupLevels: # i = "Cocain"

          # Create plot
          InitOptions = initialize_options(
            theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
            animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
            animation_easing=AnimationEasing, animation_delay=AnimationDelay,
            animation_duration_update=AnimationDurationUpdate, 
            animation_easing_update=AnimationEasingUpdate,
            animation_delay_update=AnimationDelayUpdate)

          plot_dict[i] = PyLine(init_opts = opts.InitOpts(**InitOptions))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = XVal)
          if not TimeLine:
            plot_dict[i] = plot_dict[i].add_yaxis(
              series_name = i,
              is_smooth = True,
              symbol = Symbol,
              symbol_size = SymbolSize,
              is_symbol_show = ShowSymbol,
              y_axis = yvar_dict[i],
              areastyle_opts = opts.AreaStyleOpts(opacity = Opacity),
              linestyle_opts = opts.LineStyleOpts(width = LineWidth),
              label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
            )
          else:
            plot_dict[i] = plot_dict[i].add_yaxis(
              series_name = i,
              is_smooth = True,
              symbol = Symbol,
              symbol_size = SymbolSize,
              is_symbol_show = ShowSymbol,
              y_axis = yvar_dict[i],
              areastyle_opts = opts.AreaStyleOpts(color = JsCode(JS_GradientAreaFill(GradientColors)), opacity=Opacity),
              linestyle_opts = opts.LineStyleOpts(width = LineWidth),
              label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
            )

          # Global Options
          GlobalOptions = {}
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
          GlobalOptions = configure_global_chart_options(
            global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
            brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
    
          # Final Setting of Global Options
          plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
      
          # Series Options
          plot_dict[i] = configure_marklines(
            chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
            vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

        # Facet Output
        if not TimeLine:
          
          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))

          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:
          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)

          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")


#################################################################################################


def StackedArea(dt = None,
                PreAgg = False,
                YVar = None,
                XVar = None,
                GroupVar = None,
                AggMethod = 'mean',
                YVarTrans = None,
                RenderHTML = None,
                Opacity = 0.5,
                LineWidth = 2,
                Symbol = "emptyCircle",
                SymbolSize = 6,
                ShowLabels = False,
                LabelPosition = "top",
                Theme = 'wonderland',
                BackgroundColor = None,
                Width = None,
                Height = None,
                ToolBox = True,
                Brush = True,
                DataZoom = True,
                Title = 'Stacked Area',
                TitleColor = "#fff",
                TitleFontSize = 20,
                SubTitle = None,
                SubTitleColor = "#fff",
                SubTitleFontSize = 12,
                AxisPointerType = 'cross',
                YAxisTitle = None,
                YAxisNameLocation = 'middle',
                YAxisNameGap = 70,
                XAxisTitle = None,
                XAxisNameLocation = 'middle',
                XAxisNameGap = 42,
                Legend = None,
                LegendPosRight = '0%',
                LegendPosTop = '5%',
                LegendBorderSize = 0.25,
                LegendTextColor = "#fff",
                AnimationThreshold = 2000,
                AnimationDuration = 1000,
                AnimationEasing = "cubicOut",
                AnimationDelay = 0,
                AnimationDurationUpdate = 300,
                AnimationEasingUpdate = "cubicOut",
                AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Opacity: For grouping plots. Defaults to 0.5
    LineWidth: Numeric. Default 2
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if not isinstance(YVar, list) and GroupVar is None:
      return None
    else:
      if len(YVar) == 1 and GroupVar is None:
        return None

    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in YVar:
        yaxis_options = {}
        yaxis_options['stack'] = "stack1"
        yaxis_options['series_name'] = yvar
        yaxis_options['is_smooth'] = True
        yaxis_options['symbol'] = Symbol
        yaxis_options['symbol_size'] = SymbolSize,
        yaxis_options['is_symbol_show'] = ShowSymbol
        yaxis_options['y_axis'] = yvar_dict[yvar]
        yaxis_options['linestyle_opts'] = opts.LineStyleOpts(width = LineWidth)
        yaxis_options['label_opts'] = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition)
        yaxis_options['areastyle_opts'] = opts.AreaStyleOpts(opacity = 0.5)

        c = c.add_yaxis(**yaxis_options)

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      yvar_dict = {}
      GroupLevels = dt1[GroupVar].unique().sort().to_list()
      for gv in GroupLevels:
        temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
        yvar_dict[gv] = temp[YVar].to_list()

      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyLine(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      for yvar in GroupLevels:
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          symbol = Symbol,
          symbol_size = SymbolSize,
          is_smooth = True,
          is_symbol_show = ShowSymbol,
          y_axis = yvar_dict[yvar],
          linestyle_opts = opts.LineStyleOpts(width = LineWidth),
          areastyle_opts = opts.AreaStyleOpts(opacity = Opacity),
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c


#################################################################################################


def Bar(dt = None,
        PreAgg = False,
        YVar = None,
        XVar = None,
        GroupVar = None,
        FacetRows = 1,
        FacetCols = 1,
        FacetLevels = None,
        TimeLine = False,
        AggMethod = 'mean',
        YVarTrans = None,
        RenderHTML = None,
        ShowLabels = False,
        LabelPosition = "top",
        Theme = 'wonderland',
        BackgroundColor = None,
        Width = None,
        Height = None,
        ToolBox = True,
        Brush = True,
        DataZoom = True,
        Title = 'Bar Plot',
        TitleColor = "#fff",
        TitleFontSize = 20,
        SubTitle = None,
        SubTitleColor = "#fff",
        SubTitleFontSize = 12,
        AxisPointerType = 'cross',
        YAxisTitle = None,
        YAxisNameLocation = 'middle',
        YAxisNameGap = 70,
        XAxisTitle = None,
        XAxisNameLocation = 'middle',
        XAxisNameGap = 42,
        Legend = None,
        LegendPosRight = '0%',
        LegendPosTop = '5%',
        LegendBorderSize = 0.25,
        LegendTextColor = "#fff",
        VerticalLine = None,
        VerticalLineName = 'Line Name',
        HorizontalLine = None,
        HorizontalLineName = 'Line Name',
        AnimationThreshold = 2000,
        AnimationDuration = 1000,
        AnimationEasing = "cubicOut",
        AnimationDelay = 0,
        AnimationDurationUpdate = 300,
        AnimationEasingUpdate = "cubicOut",
        AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date or categorical variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """

    # Load environment
    
    
    from pyecharts.commons.utils import JsCode
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    # No GroupVar
    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyBar(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      for yvar in YVar:
        yaxis_options = {}
        yaxis_options['series_name'] = yvar
        yaxis_options['y_axis'] = yvar_dict[yvar]
        yaxis_options['label_opts'] = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition)
        
        c = c.add_yaxis(**yaxis_options)

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyBar(init_opts = opts.InitOpts(**InitOptions))
        c = c.add_xaxis(xaxis_data = XVal)
        for yvar in GroupLevels:
          c = c.add_yaxis(
            series_name = yvar,
            y_axis = yvar_dict[yvar],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        if not Title is None:
          GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)
        
        yvar_dict = {}
        plot_dict = {}
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
          yvar_dict[gv] = temp[YVar].to_list()

        XVal = dt1[XVar].unique().to_list()

        # Create plot
        for i in GroupLevels:# i = 'Yellow-Yum'
          plot_dict[i] = PyBar(init_opts = opts.InitOpts(**InitOptions))#theme = Theme))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = XVal)
          plot_dict[i] = plot_dict[i].add_yaxis(
            series_name = i,
            y_axis = yvar_dict[i],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )
          
          # Global Options
          GlobalOptions = {}
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = f"{i}", position = "right")
  
          # Final Setting of Global Options
          plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)

        # Facet Output
        if not TimeLine:
          
          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))

          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:
          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)
          
          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")

          return tl


#################################################################################################


def StackedBar(dt = None,
               PreAgg = False,
               YVar = None,
               XVar = None,
               GroupVar = None,
               AggMethod = 'mean',
               YVarTrans = None,
               RenderHTML = None,
               ShowLabels = False,
               LabelPosition = "top",
               Theme = 'wonderland',
               BackgroundColor = None,
               Width = None,
               Height = None,
               ToolBox = True,
               Brush = True,
               DataZoom = True,
               Title = 'Stacked Bar',
               TitleColor = "#fff",
               TitleFontSize = 20,
               SubTitle = None,
               SubTitleColor = "#fff",
               SubTitleFontSize = 12,
               AxisPointerType = 'cross',
               YAxisTitle = None,
               YAxisNameLocation = 'middle',
               YAxisNameGap = 70,
               XAxisTitle = None,
               XAxisNameLocation = 'middle',
               XAxisNameGap = 42,
               Legend = None,
               LegendPosRight = '0%',
               LegendPosTop = '5%',
               LegendBorderSize = 0.25,
               LegendTextColor = "#fff",
               AnimationThreshold = 2000,
               AnimationDuration = 1000,
               AnimationEasing = "cubicOut",
               AnimationDelay = 0,
               AnimationDurationUpdate = 300,
               AnimationEasingUpdate = "cubicOut",
               AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: date or categorical variable
    GroupVar: grouping variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None
    
    if not isinstance(YVar, list) and GroupVar is None:
      return None
    else:
      if len(YVar) == 1 and GroupVar is None:
        return None

    if isinstance(YVar, list):
      if len(YVar) > 1:
        GroupVar = None

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt.select([pl.col(YVar), pl.col(XVar)])

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVar, list):
        for i in range(len(YVar)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVar[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVar, GroupVariable = GroupVar, DateVariable = XVar)
      dt1 = dt1.sort(XVar)

    if GroupVar is None:
      yvar_dict = {}
      if not isinstance(YVar, list):
        YVar = [YVar]
      for yvar in YVar:
        yvar_dict[yvar] = dt1[yvar].to_list()
        
      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyBar(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      for yvar in YVar:
        yaxis_options = {}
        yaxis_options['stack'] = "stack1"
        yaxis_options['series_name'] = yvar
        yaxis_options['y_axis'] = yvar_dict[yvar]
        yaxis_options['label_opts'] = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition)
        
        c = c.add_yaxis(**yaxis_options)

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      yvar_dict = {}
      GroupLevels = dt1[GroupVar].unique().sort().to_list()
      for gv in GroupLevels:
        temp = dt1.filter(dt1[GroupVar] == gv).select(YVar)
        yvar_dict[gv] = temp[YVar].to_list()

      XVal = dt1[XVar].unique().to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyBar(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      for yvar in GroupLevels:
        c = c.add_yaxis(
          stack = "stack1",
          series_name = yvar,
          y_axis = yvar_dict[yvar],
          label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
        )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)

      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c


#################################################################################################


def Heatmap(dt = None,
            PreAgg = False,
            YVar = None,
            XVar = None,
            MeasureVar = None,
            AggMethod = 'mean',
            MeasureVarTrans = "Identity",
            RenderHTML = None,
            ShowLabels = False,
            LabelPosition = "top",
            LabelColor = "#fff",
            Theme = 'wonderland',
            RangeColor = ["#5b5b5b5d", "#00c4ff", "#9cff00"],
            BackgroundColor = None,
            Width = None,
            Height = None,
            ToolBox = True,
            Brush = True,
            DataZoom = True,
            Title = 'Heatmap Plot',
            TitleColor = "#fff",
            TitleFontSize = 20,
            SubTitle = None,
            SubTitleColor = "#fff",
            SubTitleFontSize = 12,
            AxisPointerType = 'cross',
            YAxisTitle = None,
            YAxisNameLocation = 'middle',
            YAxisNameGap = 70,
            XAxisTitle = None,
            XAxisNameLocation = 'middle',
            XAxisNameGap = 42,
            Legend = None,
            LegendPosRight = '0%',
            LegendPosTop = '5%',
            LegendBorderSize = 0.25,
            LegendTextColor = "#fff",
            AnimationThreshold = 2000,
            AnimationDuration = 1000,
            AnimationEasing = "cubicOut",
            AnimationDelay = 0,
            AnimationDurationUpdate = 300,
            AnimationEasingUpdate = "cubicOut",
            AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: categorical variable
    XVar: categorical variable
    MeasureVar: numeric variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    MeasureVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    ShowLabels: Default False
    LabelColor = "#fff"
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    if XVar == None:
      return None
    
    if MeasureVar == None:
      return None

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(MeasureVar)])

    # Transformation
    if not MeasureVarTrans is None:
      dt1 = NumericTransformation(dt1, MeasureVar, Trans = MeasureVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = MeasureVar, GroupVariable = [YVar, XVar], DateVariable = None)
      dt1 = dt1.sort(YVar)

    # Variable Creation
    xvar_unique = dt1[XVar].unique().to_list()
    yvar_unique = dt1[YVar].unique().to_list()
    measurevar_unique = dt1[MeasureVar].unique().to_list()
    
    # Creating Cross Join from lists
    total_len = len(yvar_unique) * len(xvar_unique)
    dt2 = pl.DataFrame({
      YVar: yvar_unique * len(xvar_unique),
      XVar: xvar_unique * len(yvar_unique)
    })

    dt2 = dt2.sort(YVar)
    dt2 = dt2.join(dt1, on = [YVar, XVar], how = "left")

    max_counter = dt2.shape[0]
    data = [[0,0,0]] * max_counter
    counter = -1
    for i in range(len(xvar_unique)):# counter = 75
      temp_xval = dt1[XVar][i]
      for j in range(len(yvar_unique)):
        counter += 1
        if dt2[MeasureVar][counter] is None:
          data[counter] = [i, j, 0]
        else:
          data[counter] = [i, j, dt2[MeasureVar][counter]]

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = HeatMap(init_opts = opts.InitOpts(**InitOptions))
    c = c.add_xaxis(xvar_unique)
    c = c.add_yaxis(
      series_name = MeasureVar,
      yaxis_data = yvar_unique,
      value = data,
      label_opts = opts.LabelOpts(
        is_show = ShowLabels,
        color = "#fff",
        position = LabelPosition,
        horizontal_align = "50%")
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
    GlobalOptions['yaxis_opts'] = opts.AxisOpts(name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
    GlobalOptions['visualmap_opts'] = opts.VisualMapOpts(range_color = RangeColor),
 
    if DataZoom:
      GlobalOptions['datazoom_opts'] = get_datazoom_options()

    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def Scatter(dt = None,
            SampleSize = 15000,
            YVar = None,
            XVar = None,
            GroupVar = None,
            FacetRows = 1,
            FacetCols = 1,
            FacetLevels = None,
            TimeLine = False,
            AggMethod = 'mean',
            YVarTrans = None,
            XVarTrans = None,
            RenderHTML = None,
            LineWidth = 2,
            Symbol = "emptyCircle",
            SymbolSize = 6,
            ShowLabels = False,
            LabelPosition = "top",
            Theme = 'wonderland',
            BackgroundColor = None,
            Width = None,
            Height = None,
            ToolBox = True,
            Brush = True,
            DataZoom = True,
            Title = 'Scatter Plot',
            TitleColor = "#fff",
            TitleFontSize = 20,
            SubTitle = None,
            SubTitleColor = "#fff",
            SubTitleFontSize = 12,
            AxisPointerType = 'cross',
            YAxisTitle = None,
            YAxisNameLocation = 'middle',
            YAxisNameGap = 70,
            XAxisTitle = None,
            XAxisNameLocation = 'middle',
            XAxisNameGap = 42,
            Legend = None,
            LegendPosRight = '0%',
            LegendPosTop = '5%',
            LegendBorderSize = 0.25,
            LegendTextColor = "#fff",
            VerticalLine = None,
            VerticalLineName = 'Line Name',
            HorizontalLine = None,
            HorizontalLineName = 'Line Name',
            AnimationThreshold = 2000,
            AnimationDuration = 1000,
            AnimationEasing = "cubicOut",
            AnimationDelay = 0,
            AnimationDurationUpdate = 300,
            AnimationEasingUpdate = "cubicOut",
            AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: numeric variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    XVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """


    # Define Plotting Variable
    if YVar == None:
      return None

    # Define Plotting Variable
    if XVar == None:
      return None

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt1.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(XVar)])

    # Transformations
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())

    if not XVarTrans is None:
      dt1 = NumericTransformation(dt1, XVar, Trans = XVarTrans.lower())

    # No GroupVar
    if GroupVar is None:
      YVal = dt1[YVar].to_list()
      XVal = dt1[XVar].to_list()

      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyScatter(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      c = c.add_yaxis(
        series_name = YVar,
        symbol = Symbol,
        symbol_size = SymbolSize,
        y_axis = YVal,
        label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
      )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), type_ = "value", name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        xvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv)
          yvar_dict[gv] = temp[YVar].to_list()
          xvar_dict[gv] = temp[XVar].to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyScatter(init_opts = opts.InitOpts(**InitOptions))
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for gv in GroupLevels:
          c = c.add_xaxis(xaxis_data = xvar_dict[gv])
          c = c.add_yaxis(
            series_name = gv,
            symbol = Symbol,
            symbol_size = SymbolSize,
            y_axis = yvar_dict[gv],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        if not Title is None:
          GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), type_ = "value", name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        plot_dict = {}
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        yvar_dict = {}
        xvar_dict = {}
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv)
          yvar_dict[gv] = temp[YVar].to_list()
          xvar_dict[gv] = temp[XVar].to_list()

        # Create plot
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for i in GroupLevels:# i = 'Yellow-Yum'
          
          # Create plot
          InitOptions = initialize_options(
            theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
            animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
            animation_easing=AnimationEasing, animation_delay=AnimationDelay,
            animation_duration_update=AnimationDurationUpdate, 
            animation_easing_update=AnimationEasingUpdate,
            animation_delay_update=AnimationDelayUpdate)
          
          plot_dict[i] = PyScatter(init_opts = opts.InitOpts(**InitOptions))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = xvar_dict[i])
          plot_dict[i] = plot_dict[i].add_yaxis(
            series_name = i,
            symbol = Symbol,
            symbol_size = SymbolSize,
            y_axis = yvar_dict[i],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

          # Global Options
          GlobalOptions = {}
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
          GlobalOptions = configure_global_chart_options(
            global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
            brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
    
          # Final Setting of Global Options
          plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
      
          # Series Options
          plot_dict[i] = configure_marklines(
            chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
            vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

        # Facet Output
        if not TimeLine:
          
          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))
  
          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:
          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)

          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")

          return tl


#################################################################################################


def Scatter3D(dt = None,
              SampleSize = 15000,
              YVar = None,
              XVar = None,
              ZVar = None,
              AggMethod = 'mean',
              YVarTrans = None,
              XVarTrans = None,
              ZVarTrans = None,
              RenderHTML = None,
              ColorMapVar = "ZVar",
              SymbolSize = 6,
              Theme = 'wonderland',
              RangeColor = ["red", "white", "blue"],
              BackgroundColor = None,
              Width = None,
              Height = None,
              AnimationThreshold = 2000,
              AnimationDuration = 1000,
              AnimationEasing = "cubicOut",
              AnimationDelay = 0,
              AnimationDurationUpdate = 300,
              AnimationEasingUpdate = "cubicOut",
              AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    SampleSize: Reduce data size
    YVar: numeric variable
    XVar: numeric variable
    ZVar: numeric variable
    ColorMapVar: Choose from default "ZVar", or "XVar", "YVar"
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    XVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    ZVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    SymbolSize: Default 6
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """


    # Define Plotting Variable
    if YVar == None:
      return None

    if XVar == None:
      return None

    if ZVar == None:
      return None
    
    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Subset Columns
    dt1 = dt1.select([pl.col(YVar), pl.col(ZVar), pl.col(XVar)])

    # Transformations
    if not YVarTrans is None:
      dt1 = NumericTransformation(dt1, YVar, Trans = YVarTrans.lower())

    if not XVarTrans is None:
      dt1 = NumericTransformation(dt1, XVar, Trans = XVarTrans.lower())

    if not ZVarTrans is None:
      dt1 = NumericTransformation(dt1, ZVar, Trans = ZVarTrans.lower())

    # Build Plot
    YVal = dt1[YVar].to_list()
    XVal = dt1[XVar].to_list()
    ZVal = dt1[XVar].to_list()
    if ColorMapVar is None:
      color = ZVal
    elif ColorMapVar == "ZVar":
      color = ZVal
    elif ColorMapVar == "YVar":
      color = YVar
    elif ColorMapVar == "XVar":
      color = XVar

    symbolSize = [SymbolSize] * len(ZVal)
    data = list(zip(YVal, XVal, ZVal, color, symbolSize))

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyScatter3D(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
      series_name="",
      data = data,
      xaxis3d_opts = opts.Axis3DOpts(
        name = XVar,
        type_ = "value"
      ),
      yaxis3d_opts = opts.Axis3DOpts(
        name = YVar,
        type_ = "value"
      ),
      zaxis3d_opts = opts.Axis3DOpts(
        name = ZVar,
        type_ = "value"
      ),
      grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
    )

    c = c.set_global_opts(
      visualmap_opts = [
        opts.VisualMapOpts(
          type_ = "color",
          is_calculable = True,
          dimension = 3,
          pos_top = "10",
          max_ = max(dt1[YVar].max(), dt1[XVar].max(), dt1[ZVar].max()),
          range_color = RangeColor,
        ),
        opts.VisualMapOpts(
          type_ = "size",
          is_calculable = True,
          dimension = 4,
          range_size = [min(dt1[YVar].min(), dt1[XVar].min(), dt1[ZVar].min()), max(dt1[YVar].max(), dt1[XVar].max(), dt1[ZVar].max())],
        ),
      ]
    )

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c


#################################################################################################


def Copula3D(dt = None,
             SampleSize = 15000,
             YVar = None,
             XVar = None,
             ZVar = None,
             AggMethod = 'mean',
             RenderHTML = None,
             ColorMapVar = "ZVar",
             SymbolSize = 100,
             RangeColor = ["red", "white", "blue"],
             Theme = 'wonderland',
             BackgroundColor = None,
             Width = None,
             Height = None,
             AnimationThreshold = 2000,
             AnimationDuration = 1000,
             AnimationEasing = "cubicOut",
             AnimationDelay = 0,
             AnimationDurationUpdate = 300,
             AnimationEasingUpdate = "cubicOut",
             AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    SampleSize: Reduce data size
    YVar: numeric variable
    XVar: numeric variable
    ZVar: numeric variable
    ColorMapVar: Choose from default "ZVar", or "XVar", "YVar"
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    RenderHTML: None or a quoted file name
    SymbolSize: Default 6
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    if XVar == None:
      return None

    if ZVar == None:
      return None

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Subset Columns
    dt1 = dt1.select([pl.col(YVar), pl.col(ZVar), pl.col(XVar)])

    # Transformations
    dt1 = NumericTransformation(dt1, YVar, Trans = "perc_rank")
    dt1 = NumericTransformation(dt1, XVar, Trans = "perc_rank")
    dt1 = NumericTransformation(dt1, ZVar, Trans = "perc_rank")

    # Build Plot
    YVal = dt1[YVar].to_list()
    XVal = dt1[XVar].to_list()
    ZVal = dt1[ZVar].to_list()
    if ColorMapVar is None:
      color = ZVal
    elif ColorMapVar == "ZVar":
      color = ZVal
    elif ColorMapVar == "YVar":
      color = YVar
    elif ColorMapVar == "XVar":
      color = XVar

    symbolSize = [SymbolSize] * len(ZVal)
    data = list(zip(YVal, XVal, ZVal, color, symbolSize))

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyScatter3D(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
      series_name="",
      data = data,
      xaxis3d_opts = opts.Axis3DOpts(
        name = XVar,
        type_ = "value"
      ),
      yaxis3d_opts = opts.Axis3DOpts(
        name = YVar,
        type_ = "value"
      ),
      zaxis3d_opts = opts.Axis3DOpts(
        name = ZVar,
        type_ = "value"
      ),
      grid3d_opts = opts.Grid3DOpts(width=100, height=100, depth=100),
    )

    c = c.set_global_opts(
      visualmap_opts = [
        opts.VisualMapOpts(
          type_ = "color",
          is_calculable = True,
          dimension = 3,
          pos_top = "10",
          max_ = max(dt1[YVar].max(), dt1[XVar].max(), dt1[ZVar].max()),
          range_color = RangeColor,
        ),
        opts.VisualMapOpts(
          type_ = "size",
          is_calculable = True,
          dimension = 4,
          range_size = [min(dt1[YVar].min(), dt1[XVar].min(), dt1[ZVar].min()), max(dt1[YVar].max(), dt1[XVar].max(), dt1[ZVar].max())],
        ),
      ]
    )

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c


#################################################################################################


def Copula(dt = None,
           SampleSize = 15000,
           YVar = None,
           XVar = None,
           GroupVar = None,
           FacetRows = 1,
           FacetCols = 1,
           FacetLevels = None,
           TimeLine = False,
           AggMethod = 'mean',
           RenderHTML = None,
           LineWidth = 2,
           Symbol = "emptyCircle",
           SymbolSize = 6,
           ShowLabels = False,
           LabelPosition = "top",
           Theme = 'wonderland',
           BackgroundColor = None,
           Width = None,
           Height = None,
           ToolBox = True,
           Brush = True,
           DataZoom = True,
           Title = 'Copula Plot',
           TitleColor = "#fff",
           TitleFontSize = 20,
           SubTitle = None,
           SubTitleColor = "#fff",
           SubTitleFontSize = 12,
           AxisPointerType = 'cross',
           YAxisTitle = None,
           YAxisNameLocation = 'middle',
           YAxisNameGap = 70,
           XAxisTitle = None,
           XAxisNameLocation = 'middle',
           XAxisNameGap = 42,
           Legend = None,
           LegendPosRight = '0%',
           LegendPosTop = '5%',
           LegendBorderSize = 0.25,
           LegendTextColor = "#fff",
           VerticalLine = None,
           VerticalLineName = 'Line Name',
           HorizontalLine = None,
           HorizontalLineName = 'Line Name',
           AnimationThreshold = 2000,
           AnimationDuration = 1000,
           AnimationEasing = "cubicOut",
           AnimationDelay = 0,
           AnimationDurationUpdate = 300,
           AnimationEasingUpdate = "cubicOut",
           AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: numeric variable
    XVar: numeric variable
    GroupVar: grouping variable
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    TimeLine: Logical. When True, individual plots will transition from one group level to the next
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    RenderHTML: None or a quoted file name
    Symbol: Default "Circle", "EmptyCircle", "SquareEmpty", "Square", "Rounded", "Rectangle", "EmptyRounded", "Rectangle", "Triangle", "EmptyTriangle", "Diamond", "EmptyDiamond", "Pin", "EmptyPin", "Arrow", "EmptyArrow"
    SymbolSize: Default 6
    ShowLabels: Default False
    LabelPosition: "top", "center", "left", "right", "bottom"
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    AxisPointerType: 'cross' 'line', 'shadow', or None
    YAxisTitle: Title for the YAxis. If none, then YVar will be the Title
    YAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    YAxisNameGap: offsetting where the title ends up. For 'middle', default is 15
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    XAxisNameLocation: Where the label resides. 'end', 'middle', 'start'
    XAxisNameGap: offsetting where the title ends up. For 'middle', default is 42
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Define Plotting Variable
    if YVar == None:
      return None

    if XVar == None:
      return None

    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Subset Columns
    if not GroupVar is None:
      dt1 = dt1.select([pl.col(YVar), pl.col(XVar), pl.col(GroupVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(XVar)])

    # Transformations
    dt1 = NumericTransformation(dt1, YVar, Trans = 'perc_rank')
    dt1 = NumericTransformation(dt1, XVar, Trans = 'perc_rank')

    # No GroupVar
    if GroupVar is None:
      YVal = dt1[YVar].to_list()
      XVal = dt1[XVar].to_list()
      
      # Create plot
      InitOptions = initialize_options(
        theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
        animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
        animation_easing=AnimationEasing, animation_delay=AnimationDelay,
        animation_duration_update=AnimationDurationUpdate, 
        animation_easing_update=AnimationEasingUpdate,
        animation_delay_update=AnimationDelayUpdate)

      # Create plot
      c = PyScatter(init_opts = opts.InitOpts(**InitOptions))
      c = c.add_xaxis(xaxis_data = XVal)
      if not Symbol is None:
        ShowSymbol = True
      else:
        ShowSymbol = False
      c = c.add_yaxis(
        series_name = YVar,
        symbol = Symbol,
        symbol_size = SymbolSize,
        y_axis = YVal,
        label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
      )

      # Global Options
      GlobalOptions = {}
      GlobalOptions['legend_opts'] = configure_legend_options(
        legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
        legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
      if not Title is None:
        GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

      GlobalOptions['xaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), type_ = "value", name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
      GlobalOptions['yaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
      GlobalOptions = configure_global_chart_options(
        global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
        brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      c = configure_marklines(
        chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
        vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
        
      # Render html
      if RenderHTML:
        c.render(f"{RenderHTML}.html")
    
      return c

    # Grouping Case
    else:

      # No Facet Case
      if not TimeLine and FacetCols == 1 and FacetRows == 1:
        
        yvar_dict = {}
        xvar_dict = {}
        GroupLevels = dt1[GroupVar].unique().sort().to_list()
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv)
          yvar_dict[gv] = temp[YVar].to_list()
          xvar_dict[gv] = temp[XVar].to_list()

        # Create plot
        InitOptions = initialize_options(
          theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
          animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
          animation_easing=AnimationEasing, animation_delay=AnimationDelay,
          animation_duration_update=AnimationDurationUpdate, 
          animation_easing_update=AnimationEasingUpdate,
          animation_delay_update=AnimationDelayUpdate)

        # Create plot
        c = PyScatter(init_opts = opts.InitOpts(**InitOptions))
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for gv in GroupLevels:
          c = c.add_xaxis(xaxis_data = xvar_dict[gv])
          c = c.add_yaxis(
            series_name = gv,
            symbol = Symbol,
            symbol_size = SymbolSize,
            y_axis = yvar_dict[gv],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

        # Global Options
        GlobalOptions = {}
        GlobalOptions['legend_opts'] = configure_legend_options(
          legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
          legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)
  
        GlobalOptions['xaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), type_ = "value", name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
        GlobalOptions['yaxis_opts'] = opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True), name = YAxisTitle, name_location = YAxisNameLocation, name_gap = YAxisNameGap)
        GlobalOptions = configure_global_chart_options(
          global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
          brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
  
        # Final Setting of Global Options
        c = c.set_global_opts(**GlobalOptions)
    
        # Series Options
        c = configure_marklines(
          chart=c, horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
          vertical_line=VerticalLine, vertical_line_name=VerticalLineName)
          
        # Render html
        if RenderHTML:
          c.render(f"{RenderHTML}.html")
      
        return c

      # Facet Case
      else:
        
        plot_dict = {}
        if not TimeLine:
          if FacetLevels is None:
            GroupLevels = dt1[GroupVar].unique().sort().to_list()
            GroupLevels = GroupLevels[0:(FacetCols * FacetRows)]
          else:
            GroupLevels = FacetLevels[0:(FacetCols * FacetRows)]
        else:
          GroupLevels = dt1[GroupVar].unique().sort().to_list()

        yvar_dict = {}
        xvar_dict = {}
        for gv in GroupLevels:
          temp = dt1.filter(dt1[GroupVar] == gv)
          yvar_dict[gv] = temp[YVar].to_list()
          xvar_dict[gv] = temp[XVar].to_list()

        # Create plot
        if not Symbol is None:
          ShowSymbol = True
        else:
          ShowSymbol = False
        for i in GroupLevels:# i = 'Yellow-Yum'
          
          # Create plot
          InitOptions = initialize_options(
            theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
            animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
            animation_easing=AnimationEasing, animation_delay=AnimationDelay,
            animation_duration_update=AnimationDurationUpdate, 
            animation_easing_update=AnimationEasingUpdate,
            animation_delay_update=AnimationDelayUpdate)
          
          plot_dict[i] = PyScatter(init_opts = opts.InitOpts(**InitOptions))
          plot_dict[i] = plot_dict[i].add_xaxis(xaxis_data = xvar_dict[i])
          plot_dict[i] = plot_dict[i].add_yaxis(
            series_name = i,
            symbol = Symbol,
            symbol_size = SymbolSize,
            y_axis = yvar_dict[i],
            label_opts = opts.LabelOpts(is_show = ShowLabels, position = LabelPosition),
          )

          # Global Options
          GlobalOptions = {}
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap, axislabel_opts=opts.LabelOpts(rotate=45))
          GlobalOptions = configure_global_chart_options(
            global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
            brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)
    
          # Final Setting of Global Options
          plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)
      
          # Series Options
          plot_dict[i] = configure_marklines(
            chart=plot_dict[i], horizontal_line=HorizontalLine, horizontal_line_name=HorizontalLineName,
            vertical_line=VerticalLine, vertical_line_name=VerticalLineName)

        # Facet Output
        if not TimeLine:

          # Setup Grid Output
          facet_vals = FacetGridValues(
            FacetRows = FacetRows,
            FacetCols = FacetCols,
            Legend = Legend,
            LegendSpace = 10,
            Width = Width,
            Height = Height)
          if not Width:
            Width = "1250px"
          if not Height:
            Height = "750px"
          grid = Grid(init_opts=opts.InitOpts(theme=Theme, width=f"{int(Width.replace('px', '')) * FacetCols / math.sqrt(FacetCols)}px", height=f"{int(Height.replace('px', '')) * FacetRows}px"))
          counter = -1
          for i in GroupLevels:
            counter += 1
            grid = grid.add(
              plot_dict[i],
              grid_opts = opts.GridOpts(
                pos_left = f"{facet_vals['left'][counter]}%",
                pos_top = f"{facet_vals['top'][counter]}%",
                width = f"{facet_vals['Width_f']}%",
                height = f"{facet_vals['Height_f']}%"))

          # Render html
          if RenderHTML:
            grid.render(f"{RenderHTML}.html")

          return grid

        # TimeLine Output
        else:

          tl = Timeline()
          for i in GroupLevels:
            tl.add(plot_dict[i], i)

          # Render html
          if RenderHTML:
            tl.render(f"{RenderHTML}.html")
    
          return tl


#################################################################################################


def Parallel(dt = None,
             SampleSize = 15000,
             Vars = None,
             VarsTrans = None,
             RenderHTML = None,
             SymbolSize = 6,
             Opacity = 0.05,
             LineWidth = 0.20,
             Theme = 'wonderland',
             BackgroundColor = None,
             Width = None,
             Height = None,
             Title = 'Parallel Plot',
             TitleColor = "#fff",
             TitleFontSize = 20,
             SubTitle = None,
             SubTitleColor = "#fff",
             SubTitleFontSize = 12,
             AnimationThreshold = 2000,
             AnimationDuration = 1000,
             AnimationEasing = "cubicOut",
             AnimationDelay = 0,
             AnimationDurationUpdate = 300,
             AnimationEasingUpdate = "cubicOut",
             AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    SampleSize: Reduce data size
    Vars: numeric variables
    VarsTrans: list of transformations
    RenderHTML: None or a quoted file name
    SymbolSize: Default 6
    Opacity: Default 0.05
    LineWidth: Default 0.20
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """


    # Define Plotting Variable
    if Vars == None:
      return None
    
    # Cap number of records and define dt1
    dt1 = cap_records(dt, sample_size=SampleSize)

    # Subset Columns
    dt1 = dt1.select(Vars)

    # Transformations
    if not VarsTrans is None:
      counter = -1
      for v in Vars:
        counter += 1
        dt1 = NumericTransformation(dt1, v, Trans = VarsTrans[counter])

    # Schema
    parallel_axis = []
    for dim, name in enumerate(Vars):
      axis = {"dim": dim, "name": name}
      parallel_axis.append(axis)

    # Data Prep
    data_dict = {}
    for v in Vars:
      data_dict[v] = dt1[v].to_list()

    data = list(zip(*data_dict.values()))

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyParallel(init_opts = opts.InitOpts(**InitOptions))
    c = c.add_schema(schema = parallel_axis)
    c = c.add(
      series_name = "",
      data = data,
      linestyle_opts = opts.LineStyleOpts(width = LineWidth, opacity = Opacity),
    )

    GlobalOptions = {}
    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c


#################################################################################################


def Funnel(CategoryVar = None,
           ValuesVar = None,
           RenderHTML = None,
           SeriesLabel = "Funnel Data",
           SortStyle = 'decending',
           Theme = 'wonderland',
           BackgroundColor = None,
           Width = None,
           Height = None,
           Title = 'Funnel',
           TitleColor = "#fff",
           TitleFontSize = 20,
           SubTitle = None,
           SubTitleColor = "#fff",
           SubTitleFontSize = 12,
           Legend = None,
           LegendPosRight = '0%',
           LegendPosTop = '5%',
           LegendBorderSize = 0.25,
           LegendTextColor = "#fff",
           AnimationThreshold = 2000,
           AnimationDuration = 1000,
           AnimationEasing = "cubicOut",
           AnimationDelay = 0,
           AnimationDurationUpdate = 300,
           AnimationEasingUpdate = "cubicOut",
           AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    CategoryVar: List. Category labels for funnel
    ValuesVar: List. Values for the funnel
    SortStyle: Default "decending". Otherwise, "ascending"
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Title: Plot title
    TitleColor: Font color. Default "#fff" 
    TitleFontSize: Font size. Default = 20
    SeriesLabel: For hover data
    RenderHTML: None or a quoted file name
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = (
      PyFunnel(init_opts = opts.InitOpts(**InitOptions))
      .add(SeriesLabel, [list(z) for z in zip(CategoryVar, ValuesVar)], label_opts = opts.LabelOpts(position="inside"), sort_ = SortStyle)
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
 
    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c


#################################################################################################


def Bar3D(dt = None,
          PreAgg = False,
          YVar = None,
          XVar = None,
          ZVar = None,
          AggMethod = 'mean',
          ZVarTrans = None,
          RenderHTML = None,
          Theme = 'wonderland',
          BarColors = ["#00b8ff", "#0097e1", "#0876b8", "#004fa7", "#012e6d"],
          BackgroundColor = "#000",
          Width = None,
          Height = None,
          ToolBox = True,
          Brush = True,
          DataZoom = True,
          Title = 'Bar3D Plot',
          TitleColor = "#fff",
          TitleFontSize = 20,
          SubTitle = None,
          SubTitleColor = "#fff",
          SubTitleFontSize = 12,
          Legend = 'top',
          LegendPosRight = '0%',
          LegendPosTop = '5%',
          LegendBorderSize = 0.25,
          LegendTextColor = "#fff",
          AnimationThreshold = 2000,
          AnimationDuration = 1000,
          AnimationEasing = "cubicOut",
          AnimationDelay = 0,
          AnimationDurationUpdate = 300,
          AnimationEasingUpdate = "cubicOut",
          AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVar: Categorical variable
    XVar: Categorical variable
    ZVar: Numeric variable
    AggMethod: Aggregation method. Choose from count, mean, median, sum, sd, skewness, kurtosis, CoeffVar
    ZVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank
    RenderHTML: None or a quoted file name
    Title: title of plot in quotes
    TitleColor: Color of title in hex. Default "#fff"
    TitleFontSize: Font text size. Default 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    LegendBorderSize: Numeric. Default is 1. Choose 0 to not show one
    LegendTextColor: Text color of legend labels. Default '#fff'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BarColors: Color scaling for bar heights
    BackgroundColor: background color
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    

    # Subset Columns
    dt1 = dt.select([pl.col(YVar), pl.col(XVar), pl.col(ZVar)])
    
    # Transformation
    if not ZVarTrans is None:
      dt1 = NumericTransformation(dt1, ZVar, Trans = ZVarTrans.lower())
  
    # Agg Data
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = ZVar, GroupVariable = [YVar, XVar], DateVariable = None)
      dt1 = dt1.sort(YVar)

    XVal = dt1[XVar].unique().to_list()
    YVal = dt1[YVar].unique().to_list()

    # Creating Cross Join from lists
    total_len = len(YVal) * len(XVal)
    dt2 = pl.DataFrame({
      YVar: YVal * len(XVal),
      XVar: XVal * len(YVal)
    })

    dt2 = dt2.sort(YVar)
    dt2 = dt2.join(dt1, on = [YVar, XVar], how = "left")

    max_counter = dt2.shape[0]
    data = [[0,0,0]] * max_counter
    counter = -1
    for i in range(len(XVal)):# counter = 75
      temp_xval = dt1[XVar][i]
      for j in range(len(YVal)):
        counter += 1
        if dt2[ZVar][counter] is None:
          data[counter] = [i, j, 0]
        else:
          data[counter] = [i, j, dt2[ZVar][counter]]

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    # Create plot
    c = PyBar3D(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
      "Bar3D Data",
      data,
      xaxis3d_opts = opts.Axis3DOpts(XVal, type_ = "category"),
      yaxis3d_opts = opts.Axis3DOpts(YVal, type_ = "category"),
      zaxis3d_opts = opts.Axis3DOpts(type_ = "value"),
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['visualmap_opts'] = opts.VisualMapOpts(max_ = dt1[ZVar].max(), range_color = BarColors)
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    if not Title is None:
      GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)

    GlobalOptions = configure_global_chart_options(
      global_options=GlobalOptions, axis_pointer_type=None,
      brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

    # Final Setting of Global Options
    c = c.set_global_opts(**GlobalOptions)
      
    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")
  
    return c


#################################################################################################


def River(dt = None,
          PreAgg = False,
          YVars = None,
          DateVar = None,
          GroupVar = None,
          AggMethod = "sum",
          YVarTrans = None,
          RenderHTML = None,
          Theme = 'wonderland',
          BackgroundColor = None,
          ToolBox = True,
          Brush = True,
          DataZoom = True,
          Width = None,
          Height = None,
          AxisPointerType = "cross",
          Title = "River Plot",
          TitleColor = "#fff",
          TitleFontSize = 20,
          SubTitle = None,
          SubTitleColor = "#fff",
          SubTitleFontSize = 12,
          Legend = None,
          LegendPosRight = '0%',
          LegendPosTop = '5%',
          LegendBorderSize = 0.25,
          LegendTextColor = "#fff",
          AnimationThreshold = 2000,
          AnimationDuration = 1000,
          AnimationEasing = "cubicOut",
          AnimationDelay = 0,
          AnimationDurationUpdate = 300,
          AnimationEasingUpdate = "cubicOut",
          AnimationDelayUpdate = 0):
    
    """
    # Parameters
    dt: polars dataframe
    PreAgg: Set to True if your data is already aggregated. Default is False
    YVars: Numeric variables
    DateVar: XAxis variable
    GroupVar: Optional categorical variable. Will be ignored if multiple YVars are passed
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, logmin, sqrt, asinh, and perc_rank. Provide a list if you have multiple YVars and want transformations for each of them
    AxisPointerType: 'cross' 'line', 'shadow', or None
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    BackgroundColor: background color
    Title: Plot title
    TitleColor: Font color. Default "#fff" 
    TitleFontSize: Font size. Default = 20
    SubTitle: text underneath main title
    SubTitleColor: Subtitle color of text. Default "#fff"
    SubTitleFontSize: Font text size. Default 12
    Legend: Plot legend position. "top", "right", or None
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    Width: Default None. Otherwise, use something like this "1000px"
    Height: Default None. Otherwise, use something like this "600px"
    RenderHTML: None or a quoted file name
    AnimationThreshold: Default 2000
    AnimationDuration: Default 1000
    AnimationEasing: Default 'cubicOut'. 'linear', 'quadraticIn', 'quadraticInOut', 'cubicIn', 'cubicOut', 'cubicInOut', 'quarticIn', 'quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'quinticInOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut', 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut', 'backIn', 'backOut', 'backInOut', 'bounceIn', 'bounceOut', 'bounceInOut'
    AnimationDelay: Default 0
    AnimationDurationUpdate: Default 300
    AnimationEasingUpdate: Default "cubicOut"
    AnimationDelayUpdate: Default 0
    """
    
    from itertools import chain

    # Subset Columns
    if isinstance(YVars, list):
      cols = YVars.copy()
    else:
      cols = [YVars]
    cols.append(DateVar)      
    if not GroupVar is None:
      cols.append(GroupVar)

    dt1 = dt.select(cols)
    if not PreAgg:
      dt1 = PolarsAggregation(dt1, AggMethod, NumericVariable = YVars, GroupVariable = GroupVar, DateVariable = DateVar)

    # Transformation
    if not YVarTrans is None:
      if isinstance(YVars, list):
        for i in range(len(YVars)):# i = 0
          if not YVarTrans[i] is None:
            dt1 = NumericTransformation(dt1, YVars[i], Trans = YVarTrans[i].lower())
      else:
        dt1 = NumericTransformation(dt1, YVars, Trans = YVarTrans.lower())

    if isinstance(YVars, list):
      if len(YVars) > 1:
        x_data = YVars
        dt2 = dt1.unpivot(index = DateVar, on = YVars)
        dt2 = dt2.rename({"variable": "Series", "value": "Values"})
        DateVal = dt2[DateVar].to_list()
        SeriesVal = dt2["Series"].to_list()
        ValuesVal = dt2["Values"].to_list()
        data = [[DateVal[i], ValuesVal[i], SeriesVal[i]] for i in range(min(len(DateVal), len(ValuesVal), len(SeriesVal)))]
      else:
        x_data = dt1[GroupVar].unique().sort().to_list()
        DateVal = dt1[DateVar].to_list()
        GroupVal = dt1[GroupVar].to_list()
        YVal = dt1[YVars].to_list()
        data = [[DateVal[i], YVal[i], GroupVal[i]] for i in range(min(len(DateVal), len(YVal), len(GroupVal)))]
    else:
      x_data = dt1[GroupVar].unique().sort().to_list()
      DateVal = dt1[DateVar].to_list()
      GroupVal = dt1[GroupVar].to_list()
      YVal = dt1[YVars].to_list()
      data = [[DateVal[i], YVal[i], GroupVal[i]] for i in range(min(len(DateVal), len(YVal), len(GroupVal)))]

    # Create plot
    InitOptions = initialize_options(
      theme=Theme, width=Width, height=Height, background_color=BackgroundColor, 
      animation_threshold=AnimationThreshold, animation_duration=AnimationDuration,
      animation_easing=AnimationEasing, animation_delay=AnimationDelay,
      animation_duration_update=AnimationDurationUpdate, 
      animation_easing_update=AnimationEasingUpdate,
      animation_delay_update=AnimationDelayUpdate)

    c = ThemeRiver(init_opts = opts.InitOpts(**InitOptions))
    c = c.add(
      series_name = x_data,
      data = data,
      singleaxis_opts = opts.SingleAxisOpts(
          pos_top = "50", pos_bottom = "50", type_ = "time"
      )
    )

    # Global Options
    GlobalOptions = {}
    GlobalOptions['legend_opts'] = configure_legend_options(
      legend=Legend, legend_pos_right=LegendPosRight, legend_pos_top=LegendPosTop,
      legend_border_size=LegendBorderSize, legend_text_color=LegendTextColor)

    GlobalOptions['title_opts'] = get_title_options(Title, SubTitle, TitleColor, SubTitleColor, TitleFontSize, SubTitleFontSize)
    GlobalOptions = configure_global_chart_options(
      global_options=GlobalOptions, axis_pointer_type=AxisPointerType,
      brush=Brush, data_zoom=DataZoom, toolbox=ToolBox)

    c = c.set_global_opts(**GlobalOptions)

    # Render html
    if RenderHTML:
      c.render(f"{RenderHTML}.html")

    return c
