import QuickEcharts

def Histogram(Render = 'jupyter_lab',
              dt = None,
              SampleSize = None,
              YVar = None,
              GroupVar = None,
              YVarTrans = "Identity", # Log, Sqrt, Asinh
              Title = 'Histogram',
              XAxisTitle = None,
              Theme = 'wonderland',
              NumberBins = 20,
              CategoryGap = "10%",
              HorizonalLine = None,
              HorizonalLineName = 'Line Name'):
    
    """
    # Parameters
    Render: "html", which save an html file, or notebook of choice, 'jupyter_lab', 'jupyter_Render', 'nteract', 'zeppelin'
    dt: polars dataframe
    YVar: numeric variable for histogram
    GroupVar: grouping variable for histogram
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, sqrt, and asinh
    Title: title of plot in quotes
    XAxisTitle: Title for the XAxis. If none, then YVar will be the Title
    Theme: theme for echarts colors. Choose from: 'chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'
    NumberBins: number of histogram bins. Default is 20
    CategoryGap: amount of spacing between bars
    HorizonalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizonalLineName: add a series name for the horizontal line
    """

    # Render = "html" 'jupyter_lab'

    # Load environment
    from pyecharts.globals import CurrentConfig, RenderType 
    if Render.lower() != 'jupyter_notebook' and Render.lower() != 'html':
      CurrentConfig.Render_TYPE = Render.lower()
    
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    import polars as pl
    import math

    # SampleSize = 100000
    # XVar = None
    # YVar = 'Daily Liters'
    # GroupVar = None
    # YVarTrans = "Identity"
    # XVarTrans = "Identity"
    # Theme = 'wonderland'
    # NumberBins = 20
    # CategoryGap = "10%"
    # HorizonalLine = 500
    # HorizonalLineName = 'Yo Yo Daddyo'
    # dt = pl.read_csv("C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv")
    
    if XAxisTitle == None:
      XAxisTitle = YVar

    # Cap number of records and define dt1
    if SampleSize != None:
      if dt.shape[0] > SampleSize:
        dt1 = dt.sample(n = SampleSize, shuffle = True)
      else:
        dt1 = dt.clone()
    else:
      dt1 = dt.clone()

    # Define Plotting Variable
    if YVar == None:
      return NULL

    # Subset Columns
    if GroupVar == None:
      dt1 = dt1.select([pl.col(YVar)])
    else:
      dt1 = dt1.select([pl.col(YVar), pl.col(GroupVar)])

    # Transformation
    # "Asinh" "Log" "Sqrt"
    trans = YVarTrans.lower()
    if trans != "identity":
      if trans == "sqrt":
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.sqrt))
      elif trans == 'log':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.log))
      elif trans == 'asinh':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.asinh))
  
    # Create histogram data
    if GroupVar == None:
      Min = dt1.select(pl.min(YVar))
      Max = dt1.select(pl.max(YVar))
      Range = (Max - Min).to_series()[0]
      if Range < NumberBins:
        acc = round(Range / NumberBins, ndigits = 2)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.count(YVar))
        dt1 = dt1.sort("Buckets")
      else:
        acc = math.ceil(Range / NumberBins)
        dt1 = dt1.with_columns(Buckets = pl.col(YVar) / acc)
        dt1 = dt1.with_columns(Buckets = dt1['Buckets'].round() * acc)
        dt1 = dt1.group_by("Buckets").agg(pl.count(YVar))
        dt1 = dt1.sort("Buckets")

    # else:
    #   levs = unique(as.character(dt1[[GroupVar]]))
    #   gg = list()
    #   for i in levs: # i = levs[1]
    #     temp = dt1[get(GroupVar) == eval(i)]
    #     Min = temp[, min(get(YVar), na.rm = TRUE)]
    #     Max = temp[, max(get(YVar), na.rm = TRUE)]
    #     Range = Max - Min
    #     if Range < NumberBins:
    #       acc = round(Range / NumberBins, 2)
    #     else:
    #       acc = ceiling(Range / NumberBins)
    #     
    #     temp[, Buckets := round(get(YVar) / acc) * acc]
    #     gg[[i]] = temp[, .N, by = c("Buckets",GroupVar)][order(Buckets)]
    #   
    #   dt1 = data.table::rbindlist(gg)
    
    # Define data elements
    Buckets = dt1['Buckets'].to_list()
    YVar = dt1[YVar].to_list()
    
    # Create plot
    c = Bar(init_opts = opts.InitOpts(theme = Theme))
    c = c.add_xaxis(Buckets)
    c = c.add_yaxis('YVar', YVar, stack = "stack1", category_gap = CategoryGap)

    # Global Options
    c = c.set_global_opts(
        title_opts = opts.TitleOpts(title = Title),
        xaxis_opts = opts.AxisOpts(name = XAxisTitle),
        toolbox_opts = opts.ToolboxOpts(),
        brush_opts = opts.BrushOpts(),
        datazoom_opts = [
          opts.DataZoomOpts(
            range_start = 0,
            range_end = 100),
          opts.DataZoomOpts(
            type_="inside")],
    )
    
    # Series Options
    if not HorizonalLine is None:
        c = c.set_series_opts(
            markline_opts = opts.MarkLineOpts(
               data = [opts.MarkLineItem(y = HorizonalLine, name = HorizonalLineName)]
            ),
        )
    
    if Render.lower() == "html":
      c.render()
    
    return c



# Create plot
c = Bar(init_opts = opts.InitOpts(theme = Theme))
c = c.add_xaxis(Buckets)
c = c.add_yaxis('YVar', YVar, stack = "stack1", category_gap = CategoryGap)

# Global Options
c = c.set_global_opts(
    title_opts = opts.TitleOpts(title = Title),
    xaxis_opts = opts.AxisOpts(name = XAxisTitle),
    toolbox_opts = opts.ToolboxOpts(),
    brush_opts = opts.BrushOpts(),
    datazoom_opts = [
      opts.DataZoomOpts(
        range_start = 0,
        range_end = 100),
      opts.DataZoomOpts(
        type_="inside")],
)



