import polars as pl
from datetime import datetime
from QuickEcharts import Charts
import pyecharts


def _get_data():
    df = pl.DataFrame(
        {
            "integer": [1, 2, 3, 4, 5, 6],
            "date": [
                datetime(2025, 1, 1),
                datetime(2025, 1, 2),
                datetime(2025, 1, 3),
                datetime(2025, 1, 4),
                datetime(2025, 1, 5),
                datetime(2025, 1, 6),
            ],
            "float": [4.0, 5.0, 6.0, 7.0, 8.0, 9.0],
            "string": ["a", "b", "c", "a", "b", "c"],
        }
    )
    return df


#############################################
# Numeric Transformation Options
#############################################
def test_NumericTransformation_log():
    df = _get_data()
    x = Charts.NumericTransformation(df, "integer", "log")
    assert x['integer'].sum() <= 6.58 and x['integer'].sum() >= 6.57

def test_NumericTransformation_sqrt():
    df = _get_data()
    x = Charts.NumericTransformation(df, "integer", "sqrt")
    assert x['integer'].sum() <= 10.84 and x['integer'].sum() >= 10.83

def test_NumericTransformation_logmin():
    df = _get_data()
    x = Charts.NumericTransformation(df, "integer", "logmin")
    assert x['integer'].sum() <= 9.915 and x['integer'].sum() >= 9.91

def test_NumericTransformation_asinh():
    df = _get_data()
    x = Charts.NumericTransformation(df, "integer", "asinh")
    assert x['integer'].sum() <= 11.045 and x['integer'].sum() >= 11.040

def test_NumericTransformation_perc_rank():
    df = _get_data()
    x = Charts.NumericTransformation(df, "integer", "perc_rank")
    assert x['integer'].sum() == 3.5


#############################################
# Polars Aggregation Options
#############################################
def test_PolarsAggregation_mean():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'mean', 'integer', 'string', None)
    assert x['integer'].sum() == 10.5

def test_PolarsAggregation_sum():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'sum', 'integer', 'string', None)
    assert x['integer'].sum() == 21

def test_PolarsAggregation_median():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'median', 'integer', 'string', None)
    assert x['integer'].sum() == 10.5

def test_PolarsAggregation_sd():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'sd', 'integer', 'string', None)
    assert x['integer'].sum() <= 6.364 and x['integer'].sum() >= 6.363

def test_PolarsAggregation_skew():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'skewness', 'integer', 'string', None)
    assert x['integer'].sum() == 0.0

def test_PolarsAggregation_kurt():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'kurtosis', 'integer', 'string', None)
    assert x['integer'].sum() == -6.0

def test_PolarsAggregation_cv():
    df = _get_data()
    x = Charts.PolarsAggregation(df, 'CoeffVar', 'integer', 'string', None)
    assert x['integer'].sum() <= 4.95 and x['integer'].sum() >= 4.94


#############################################
# Facet Grid Values
#############################################
def test_FacetGridValues():
    x = Charts.FacetGridValues(FacetRows = 1, FacetCols = 1, Legend = 'top', LegendSpace = 10)
    assert x == {'top': [2.0], 'left': [5.0], 'Width_f': 79.0, 'Height_f': 81.0}

def test_FacetGridValues():
    x = Charts.FacetGridValues(FacetRows = 2, FacetCols = 2, Legend = 'top', LegendSpace = 10)
    assert x == {'top': [2.0, 2.0, 44.5, 44.5], 'left': [5.0, 56.0, 5.0, 56.0], 'Width_f': 37.0, 'Height_f': 40.5}


#############################################
# Charts
#############################################
def test_Histogram():
    df = _get_data()
    x = Charts.Histogram(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.composite_charts.grid.Grid)

def test_Density():
    df = _get_data()
    x = Charts.Density(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.composite_charts.grid.Grid)

def test_Pie():
    df = _get_data()
    x = Charts.Pie(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.pie.Pie)

def test_Rosetype():
    df = _get_data()
    x = Charts.Rosetype(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.pie.Pie)

def test_Donut():
    df = _get_data()
    x = Charts.Donut(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.pie.Pie)

def test_BoxPlot():
    df = _get_data()
    df = pl.concat([df, df, df, df])
    x = Charts.BoxPlot(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.boxplot.Boxplot)

def test_WordCloud():
    df = _get_data()
    df = pl.concat([df, df, df, df])
    x = Charts.WordCloud(dt=df, YVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.wordcloud.WordCloud)

def test_Radar():
    df = _get_data()
    x = Charts.Radar(dt=df, YVar='integer', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.radar.Radar)
    
def test_Line():
    df = _get_data()
    x = Charts.Line(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_StackedLine():
    df = _get_data()
    x = Charts.StackedLine(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_Step():
    df = _get_data()
    x = Charts.Step(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_StackedStep():
    df = _get_data()
    x = Charts.StackedStep(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_Area():
    df = _get_data()
    x = Charts.Area(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_StackedArea():
    df = _get_data()
    x = Charts.StackedArea(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.line.Line)

def test_Bar():
    df = _get_data()
    x = Charts.Bar(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.bar.Bar)

def test_StackedBar():
    df = _get_data()
    x = Charts.StackedBar(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.bar.Bar)

def test_Bar3D():
    df = _get_data()
    x = Charts.StackedBar(dt=df, YVar='integer', XVar='date', GroupVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.bar.Bar)
    
def test_Heatmap():
    df = _get_data()
    x = Charts.Heatmap(dt=df, MeasureVar='float', YVar='integer', XVar='string')
    assert isinstance(x, pyecharts.charts.basic_charts.heatmap.HeatMap)

def test_Scatter():
    df = _get_data()
    x = Charts.Scatter(dt=df, YVar='integer', XVar='float')
    assert isinstance(x, pyecharts.charts.basic_charts.scatter.Scatter)

def test_Copula():
    df = _get_data()
    x = Charts.Copula(dt=df, YVar='integer', XVar='float')
    assert isinstance(x, pyecharts.charts.basic_charts.scatter.Scatter)
    
def test_Scatter3D():
    df = _get_data()
    df = df.with_columns(float2 = pl.col('float'))
    x = Charts.Scatter3D(dt=df, YVar='integer', XVar='float', ZVar='float2')
    assert isinstance(x, pyecharts.charts.three_axis_charts.scatter3D.Scatter3D)

def test_Copula3D():
    df = _get_data()
    df = df.with_columns(float2 = pl.col('float'))
    df = df.with_columns(float3 = pl.col('float'))
    x = Charts.Copula3D(dt=df, YVar='float3', XVar='float', ZVar='float2')
    assert isinstance(x, pyecharts.charts.three_axis_charts.scatter3D.Scatter3D)

def test_Parallel():
    df = _get_data()
    df = df.with_columns(float2 = pl.col('float'))
    df = df.with_columns(float3 = pl.col('float'))
    x = Charts.Parallel(dt=df, Vars=['float3','float','float2'])
    assert isinstance(x, pyecharts.charts.basic_charts.parallel.Parallel)

def test_Funnel():
    x = Charts.Funnel(CategoryVar=['A', 'B', 'C'], ValuesVar = [1,2,3])
    assert isinstance(x, pyecharts.charts.basic_charts.funnel.Funnel)

def test_River():
    df = _get_data()
    x = Charts.River(dt=df, YVars=['integer','float'], DateVar='date')
    assert isinstance(x, pyecharts.charts.basic_charts.themeriver.ThemeRiver)
