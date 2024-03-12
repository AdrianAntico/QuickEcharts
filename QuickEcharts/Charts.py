import QuickEcharts


def FacetGridValues(FacetRows = 1, FacetCols = 1, Legend = 'top', LegendSpace = 10):
  
  """
  Parameters
  FacetRows: Number of rows in the facet grid
  FacetCols: Number of columns in the facet grid
  Legend: 'top', 'bottom', or None
  LegendSpace: numeric. Defautl is 10
  """
  
  # FacetRows = 2
  # FacetCols = 2
  # Legend = 'top'
  # LegendSpace = 10
  
  # number of series
  nseries = FacetRows * FacetCols
  
  # Specified margins
  margin_trbl = {"t": 2, "r": 2, "b": 5, "l": 5}
  
  # Calculate spacings ------------------------------------------------------
  
  # introduce some spacing between panels for low dimensional grids
  if FacetRows < 10:
    v_panel_space = 10 - FacetRows 
  else:
    v_panel_space = 0

  if FacetCols < 10:
    h_panel_space = 10 - FacetCols
  else: 
    h_panel_space = 0
  
  # Maximum space for facets (depends on legend position, and space for axis labels)
  if Legend == "top":
    w_max = 100 - margin_trbl["l"] - margin_trbl["r"]
    h_max = 100 - LegendSpace - margin_trbl["b"] - margin_trbl["t"]
  elif Legend == "right":
    w_max = 100 - LegendSpace - margin_trbl["l"] - margin_trbl["r"]
    h_max = 100 - margin_trbl["b"] -margin_trbl["t"]
  else:
    w_max = 100 - margin_trbl["l"] - margin_trbl["r"]
    h_max = 100 - margin_trbl["b"] - margin_trbl["t"]
  
  
  # Total space for panels, taking between-panel spacing, legend space, and
  #   extra space for axis labels into account
  FacetRows_h_max = h_max - (v_panel_space * (FacetRows - 1)) 
  FacetCols_w_max = w_max - (h_panel_space * (FacetCols - 1))
  
  # Dimensions of each panel
  height = FacetRows_h_max / FacetRows
  width = FacetCols_w_max / FacetCols
  
  # Panel positions ---------------------------------------------------------
  
  # Offset only when legend is left or top
  top_offset = 0
  left_offset = 0
  if Legend == "top":
    top_offset = LegendSpace

  # Generate a vector for positions from the top
  top_pos_values = [0 for i in range(0,FacetRows)]
  for x in range(0,FacetRows):
    top_pos_values[x] = margin_trbl["t"] + top_offset + (x * (height + v_panel_space))

  top_pos_values_rep = top_pos_values * FacetCols
  top_pos_values_rep.sort()

  # Generate a vector for positions from the left
  left_pos_values = [0 for i in range(0, FacetCols)]
  for x in range(0, FacetCols):
    left_pos_values[x] = margin_trbl["l"] + left_offset + (x * (width + h_panel_space))

  left_pos_values_rep = left_pos_values * FacetRows
  
  return {'top': top_pos_values_rep, 'left': left_pos_values_rep, 'width': width-5, 'height': height}


# grid_vals = FacetGridValues(FacetRows = 6, FacetCols = 6, Legend = 'top', LegendSpace = 10)
# grid_vals['top'][0]


def Histogram(dt = None,
              SampleSize = None,
              YVar = None,
              GroupVar = None,
              FacetRows = 1,
              FacetCols = 1,
              FacetLevels = None,
              YVarTrans = "Identity", # Log, Sqrt, Asinh
              RenderHTML = False,
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
              Theme = 'wonderland',
              NumberBins = 20,
              CategoryGap = "10%",
              Legend = None,
              LegendPosRight = '0%',
              LegendPosTop = '5%',
              ToolBox = True,
              Brush = True,
              DataZoom = True,
              VerticalLine = None,
              VerticalLineName = 'Line Name',
              HorizontalLine = None,
              HorizontalLineName = 'Line Name'):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable for histogram
    GroupVar: grouping variable for histogram
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, sqrt, and asinh
    RenderHTML: "html", which save an html file, or notebook of choice, 'jupyter_lab', 'jupyter_Render', 'nteract', 'zeppelin'
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
    NumberBins: number of histogram bins. Default is 20
    CategoryGap: amount of spacing between bars
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    """

    # Load environment
    from pyecharts import options as opts
    from pyecharts.charts import Bar, Grid
    import polars as pl
    import math

    # SampleSize = 100000
    # YVar = 'Daily Liters'
    # GroupVar = 'Brand'
    # FacetRows = 2
    # FacetCols = 2
    # FacetLevels = None
    # YVarTrans = "Identity"
    # XAxisTitle = YVar
    # XAxisNameLocation = 'middle'
    # AxisPointerType = 'cross' # 'line', 'shadow'
    # RenderHTML = False
    # Title = 'Hist Plot'
    # TitleColor = 'fff'
    # TitleFontSize = 20
    # SubTitle = 'Subtitle'
    # SubTitleColor = 'fff'
    # SubTitleFontSize = 12
    # YVarTrans = "Identity"
    # XVarTrans = "Identity"
    # Theme = 'wonderland'
    # NumberBins = 20
    # CategoryGap = "10%"
    # Legend = None
    # LegendPosRight = '0%'
    # LegendPosTop = '5%'
    # ToolBox = True
    # Brush = True
    # DataZoom = True
    # VerticalLine = 35
    # VerticalLineName = 'bla'
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

    # Transformation: "Asinh" "Log" "Sqrt"
    trans = YVarTrans.lower()
    if trans != "identity":
      if trans == "sqrt":
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.sqrt))
      elif trans == 'log':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.log))
      elif trans == 'asinh':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.asinh))
  
    # Single Histogram, no grouping
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


      # Define data elements
      Buckets = dt1['Buckets'].to_list()
      YVar = dt1[YVar].to_list()
      
      # Create plot
      c = Bar(init_opts = opts.InitOpts(theme = Theme))
      c = c.add_xaxis(Buckets)
      c = c.add_yaxis('YVar', YVar, stack = "stack1", category_gap = CategoryGap)

      # Global Options
      GlobalOptions = {}
      if Legend == 'right':
        GlobalOptions['legend_opts'] = opts.LegendOpts(pos_right = LegendPosRight, pos_top = LegendPosTop)
      elif Legend == 'top':
        GlobalOptions['legend_opts'] = opts.LegendOpts(pos_top = LegendPosTop)
  
      if not Title is None:
        GlobalOptions['title_opts'] = opts.TitleOpts(
            title = Title, subtitle = SubTitle,
            title_textstyle_opts = opts.TextStyleOpts(
              color = TitleColor,
              font_size = TitleFontSize,
            ),
            subtitle_textstyle_opts = opts.TextStyleOpts(
              color = SubTitleColor,
              font_size = SubTitleFontSize,
            )
        )
  
      
      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
  
      if ToolBox:
        GlobalOptions['toolbox_opts'] = opts.ToolboxOpts()
      
      GlobalOptions['tooltip_opts'] = opts.TooltipOpts(trigger = "axis", axis_pointer_type = AxisPointerType)
  
      if Brush:
        GlobalOptions['brush_opts'] = opts.BrushOpts()
  
      if DataZoom:
        GlobalOptions['datazoom_opts'] = [
            opts.DataZoomOpts(
              range_start = 0,
              range_end = 100),
            opts.DataZoomOpts(
              type_="inside")]
      
      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      if not HorizontalLine is None or not VerticalLine is None:
        MarkLineDict = {}
        if not HorizontalLine is None and not VerticalLine is None:
          MarkLineDict['data'] = opts.MarkLineItem(y = HorizontalLine, name = HorizontalLineName), opts.MarkLineItem(x = VerticalLine, name = VerticalLineName)
        elif HorizontalLine is None:
          MarkLineDict['data'] = opts.MarkLineItem(x = VerticalLine, name = VerticalLineName)
        else:
          MarkLineDict['data'] = opts.MarkLineItem(y = HorizontalLine, name = HorizontalLineName)

        c = c.set_series_opts(markline_opts = opts.MarkLineOpts(**MarkLineDict))

      # Render html
      if RenderHTML:
        c.render()
    
      return c

    # Group Variable Case
    else:
      
      if not FacetLevels is None:
        levs = FacetLevels
      else:
        levs = dt1[GroupVar].unique().sort()[0:(FacetCols * FacetRows)]
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
          dt2 = dt2.group_by("Buckets").agg(pl.count(YVar))
          dt2 = dt2.sort("Buckets")
        else:
          acc = math.ceil(Range / NumberBins)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.count(YVar))
          dt2 = dt2.sort("Buckets")
       
        # Define data elements
        Buckets = dt2['Buckets'].to_list().copy()
        YVal = dt2[YVar].to_list().copy()
       
        # Create plot
        plot_dict[i] = Bar(init_opts = opts.InitOpts(theme = Theme))
        plot_dict[i] = plot_dict[i].add_xaxis(Buckets)
        plot_dict[i] = plot_dict[i].add_yaxis(YVar, YVal, stack = "stack1", category_gap = CategoryGap)

        if not Title is None:
          GlobalOptions['title_opts'] = opts.TitleOpts(title = f"{Title}")
  
        if not XAxisTitle is None:
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = f"{i}")

        plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)

    # Setup Grid Output
    grid = Grid()
    facet_vals = FacetGridValues(
      FacetRows = FacetRows,
      FacetCols = FacetCols,
      Legend = Legend,
      LegendSpace = 10)
    counter = -1
    for i in levs: # i = Levs[0]
      counter += 1
      grid = grid.add(
        plot_dict[i],
        grid_opts = opts.GridOpts(
          pos_left = f"{facet_vals['left'][counter]}%",
          pos_top = f"{facet_vals['top'][counter]}%",
          width = f"{facet_vals['width']}%",
          height = f"{facet_vals['height']}%"))

    # Render html
    if RenderHTML:
      grid.render()
  
    return grid


#################################################################################################


def Density(dt = None,
            SampleSize = None,
            YVar = None,
            GroupVar = None,
            FacetRows = 1,
            FacetCols = 1,
            FacetLevels = None,
            YVarTrans = "Identity", # Log, Sqrt, Asinh
            RenderHTML = False,
            LineWidth = 2,
            FillOpacity = 0.5,
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
            Theme = 'wonderland',
            NumberBins = 20,
            Legend = None,
            LegendPosRight = '0%',
            LegendPosTop = '5%',
            ToolBox = True,
            Brush = True,
            DataZoom = True,
            VerticalLine = None,
            VerticalLineName = 'Line Name',
            HorizontalLine = None,
            HorizontalLineName = 'Line Name'):
    
    """
    # Parameters
    dt: polars dataframe
    YVar: numeric variable for histogram
    GroupVar: grouping variable for histogram
    FacetRows: Number of rows in facet grid
    FacetCols: Number of columns in facet grid
    FacetLevels: None or supply a list of levels that will be used. The number of levels should fit into FactetRows * FacetCols grid
    YVarTrans: apply a numeric transformation on your YVar values. Choose from log, sqrt, and asinh
    RenderHTML: "html", which save an html file, or notebook of choice, 'jupyter_lab', 'jupyter_Render', 'nteract', 'zeppelin'
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
    NumberBins: number of histogram bins. Default is 20
    Legend: Choose from None, 'right', 'top'
    LegendPosRight: If Legend == 'right' you can specify location from right border. Default is '0%'
    LegendPosTop: If Legen == 'right' or 'top' you can specify distance from the top border. Default is '5%'
    ToolBox: Logical. Select True to enable toolbox for zooming and other functionality
    Brush: Logical. Select True for addition ToolBox functionality. Default is True
    DataZoom: Logical. Select True to add zoom bar on xaxis. Default is True
    VerticalLine: numeric. Add a vertical line on the plot at the value specified
    VerticalLineName: add a series name for the vertical line
    HorizontalLine: numeric. Add a horizontal line on the plot at the value specified
    HorizontalLineName: add a series name for the horizontal line
    """

    # Load environment
    from pyecharts import options as opts
    from pyecharts.charts import Bar, Grid
    import polars as pl
    import math

    # SampleSize = 100000
    # YVar = 'Daily Liters'
    # GroupVar = 'Brand'
    # FacetRows = 2
    # FacetCols = 2
    # FacetLevels = None
    # YVarTrans = "Identity"
    # XAxisTitle = YVar
    # XAxisNameLocation = 'middle'
    # AxisPointerType = 'cross' # 'line', 'shadow'
    # LineWidth = 2
    # FillOpacity = 0.5
    # RenderHTML = False
    # Title = 'Hist Plot'
    # TitleColor = 'fff'
    # TitleFontSize = 20
    # SubTitle = 'Subtitle'
    # SubTitleColor = 'fff'
    # SubTitleFontSize = 12
    # YVarTrans = "Identity"
    # XVarTrans = "Identity"
    # Theme = 'wonderland'
    # NumberBins = 20
    # Legend = None
    # LegendPosRight = '0%'
    # LegendPosTop = '5%'
    # ToolBox = True
    # Brush = True
    # DataZoom = True
    # VerticalLine = 35
    # VerticalLineName = 'bla'
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

    # Transformation: "Asinh" "Log" "Sqrt"
    trans = YVarTrans.lower()
    if trans != "identity":
      if trans == "sqrt":
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.sqrt))
      elif trans == 'log':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.log))
      elif trans == 'asinh':
        dt1 = dt1.with_columns(pl.col(YVar).map_elements(math.asinh))
  
    # Single Histogram, no grouping
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


      # Define data elements
      Buckets = dt1['Buckets'].to_list()
      YVar = dt1[YVar].to_list()
      
      # Create plot
      c = Line(init_opts = opts.InitOpts(theme = Theme))
      c = c.add_xaxis(Buckets)
      c = c.add_yaxis(
        'YVar',
        YVar,
        is_smooth = True,
        linestyle_opts = opts.LineStyleOpts(width = LineWidth),
        areastyle_opts = opts.AreaStyleOpts(opacity = FillOpacity))

      # Global Options
      GlobalOptions = {}
      if Legend == 'right':
        GlobalOptions['legend_opts'] = opts.LegendOpts(pos_right = LegendPosRight, pos_top = LegendPosTop)
      elif Legend == 'top':
        GlobalOptions['legend_opts'] = opts.LegendOpts(pos_top = LegendPosTop)
  
      if not Title is None:
        GlobalOptions['title_opts'] = opts.TitleOpts(
            title = Title, subtitle = SubTitle,
            title_textstyle_opts = opts.TextStyleOpts(
              color = TitleColor,
              font_size = TitleFontSize,
            ),
            subtitle_textstyle_opts = opts.TextStyleOpts(
              color = SubTitleColor,
              font_size = SubTitleFontSize,
            )
        )
  
      
      GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = XAxisTitle, name_location = XAxisNameLocation, name_gap = XAxisNameGap)
  
      if ToolBox:
        GlobalOptions['toolbox_opts'] = opts.ToolboxOpts()
      
      GlobalOptions['tooltip_opts'] = opts.TooltipOpts(trigger = "axis", axis_pointer_type = AxisPointerType)
  
      if Brush:
        GlobalOptions['brush_opts'] = opts.BrushOpts()
  
      if DataZoom:
        GlobalOptions['datazoom_opts'] = [
            opts.DataZoomOpts(
              range_start = 0,
              range_end = 100),
            opts.DataZoomOpts(
              type_="inside")]
      
      # Final Setting of Global Options
      c = c.set_global_opts(**GlobalOptions)
  
      # Series Options
      if not HorizontalLine is None or not VerticalLine is None:
        MarkLineDict = {}
        if not HorizontalLine is None and not VerticalLine is None:
          MarkLineDict['data'] = opts.MarkLineItem(y = HorizontalLine, name = HorizontalLineName), opts.MarkLineItem(x = VerticalLine, name = VerticalLineName)
        elif HorizontalLine is None:
          MarkLineDict['data'] = opts.MarkLineItem(x = VerticalLine, name = VerticalLineName)
        else:
          MarkLineDict['data'] = opts.MarkLineItem(y = HorizontalLine, name = HorizontalLineName)

        c = c.set_series_opts(markline_opts = opts.MarkLineOpts(**MarkLineDict))

      # Render html
      if RenderHTML:
        c.render()
    
      return c

    # Group Variable Case
    else:
      
      if not FacetLevels is None:
        levs = FacetLevels
      else:
        levs = dt1[GroupVar].unique().sort()[0:(FacetCols * FacetRows)]
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
          dt2 = dt2.group_by("Buckets").agg(pl.count(YVar))
          dt2 = dt2.sort("Buckets")
        else:
          acc = math.ceil(Range / NumberBins)
          dt2 = dt2.with_columns(Buckets = pl.col(YVar) / acc)
          dt2 = dt2.with_columns(Buckets = dt2['Buckets'].round() * acc)
          dt2 = dt2.group_by("Buckets").agg(pl.count(YVar))
          dt2 = dt2.sort("Buckets")
       
        # Define data elements
        Buckets = dt2['Buckets'].to_list().copy()
        YVal = dt2[YVar].to_list().copy()
       
        # Create plot
        plot_dict[i] = Line(init_opts = opts.InitOpts(theme = Theme))
        plot_dict[i] = plot_dict[i].add_xaxis(Buckets)
        plot_dict[i] = plot_dict[i].add_yaxis(YVar, YVal, is_smooth = True)

        if not Title is None:
          GlobalOptions['title_opts'] = opts.TitleOpts(title = f"{Title}")
  
        if not XAxisTitle is None:
          GlobalOptions['xaxis_opts'] = opts.AxisOpts(name = f"{i}")

        plot_dict[i] = plot_dict[i].set_global_opts(**GlobalOptions)

    # Setup Grid Output
    grid = Grid()
    facet_vals = FacetGridValues(
      FacetRows = FacetRows,
      FacetCols = FacetCols,
      Legend = Legend,
      LegendSpace = 10)
    counter = -1
    for i in levs: # i = Levs[0]
      counter += 1
      grid = grid.add(
        plot_dict[i],
        grid_opts = opts.GridOpts(
          pos_left = f"{facet_vals['left'][counter]}%",
          pos_top = f"{facet_vals['top'][counter]}%",
          width = f"{facet_vals['width']}%",
          height = f"{facet_vals['height']}%"))

    # Render html
    if RenderHTML:
      grid.render()
  
    return grid







