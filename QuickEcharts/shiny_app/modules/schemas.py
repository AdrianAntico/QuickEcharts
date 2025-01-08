PLOT_SCHEMAS = {
  "Area": {
      # Data settings
      "dt": {"type": "file", "label": "Data Table", "default": None},
      "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
      "YVar": {"type": "select", "label": "Y Variable", "default": None},
      "XVar": {"type": "select", "label": "X Variable", "default": None},
      "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
      "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
      "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
      "AggMethod": {
          "type": "select",
          "label": "Aggregation Method",
          "options": ["mean", "sum", "median", "max", "min"],
          "default": "mean",
      },
      "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

      # Rendering settings
      "Theme": {
          "type": "select",
          "label": "Theme",
          "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
          "default": "dark",
      },
      
      "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
      "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

      # Visual settings
      "Opacity": {"type": "slider", "label": "Opacity", "min": 0, "max": 1, "default": 0.5},
      "GradientColors": {
          "type": "multi-select",
          "label": "Gradient Colors (JSON)",
          "default": ['#06a7ff0d', '#e12191'],
          "options": [
              "#c86589", "#06a7ff0d", "#e12191", "#0926800d", "#f4a460", "#4682b4", "#8a2be2"
          ]
      },
      "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
      "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
      "LabelPosition": {
          "type": "select",
          "label": "Label Position",
          "options": ["top", "left", "right", "bottom", "inside"],
          "default": "top",
      },
  
      # Interaction settings
      "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
      "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
  
      # Title and subtitle settings
      "Title": {"type": "text", "label": "Title", "default": "Area Plot"},
      "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
      "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
      "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
      "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
      "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},
  
      # Axis settings
      "AxisPointerType": {
          "type": "select",
          "label": "Axis Pointer Type",
          "options": ["line", "shadow", "cross", "none"],
          "default": "cross",
      },
      "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
      "YAxisNameLocation": {
          "type": "select",
          "label": "Y Axis Name Location",
          "options": ["start", "middle", "end"],
          "default": "middle",
      },
      "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
      "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
      "XAxisNameLocation": {
          "type": "select",
          "label": "X Axis Name Location",
          "options": ["start", "middle", "end"],
          "default": "middle",
      },
      "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},
  
      # Legend settings
      "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
      "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
      "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
      "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
      "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  
      # Reference lines
      
      
      
      
  },
  
  "Bar": {
      # Data settings
      "dt": {"type": "file", "label": "Data Table", "default": None},
      "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
      "YVar": {"type": "select", "label": "Y Variable", "default": None},
      "XVar": {"type": "select", "label": "X Variable", "default": None},
      "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
      "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
      "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
      "AggMethod": {
          "type": "select",
          "label": "Aggregation Method",
          "options": ["mean", "sum", "median", "max", "min"],
          "default": "mean",
      },
      "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
  
      # Rendering settings
      "Theme": {
          "type": "select",
          "label": "Theme",
          "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
          "default": "dark",
      },
      
      "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
      "Height": {"type": "text", "label": "Chart Height", "default": "750px"},
  
      # Visual settings
      "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
      "LabelPosition": {
          "type": "select",
          "label": "Label Position",
          "options": ["top", "left", "right", "bottom", "inside"],
          "default": "top",
      },
  
      # Interaction settings
      "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
      "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
      
  
      # Title and subtitle settings
      "Title": {"type": "text", "label": "Title", "default": "Bar Plot"},
      "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
      "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
      "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
      "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
      "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},
  
      # Axis settings
      "AxisPointerType": {
          "type": "select",
          "label": "Axis Pointer Type",
          "options": ["line", "shadow", "cross", "none"],
          "default": "cross",
      },
      "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
      "YAxisNameLocation": {
          "type": "select",
          "label": "Y Axis Name Location",
          "options": ["start", "middle", "end"],
          "default": "middle",
      },
      "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
      "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
      "XAxisNameLocation": {
          "type": "select",
          "label": "X Axis Name Location",
          "options": ["start", "middle", "end"],
          "default": "middle",
      },
      "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},
  
      # Legend settings
      "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
      "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
      "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
      "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
      "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "BoxPlot": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 10000, "default": None},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Box Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 42},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    

  },
  
  "Copula": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": 15000},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "XVarTrans": {"type": "select", "label": "X Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Visual settings
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Copula Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },
  
  "Copula3D": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": 15000},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "ZVar": {"type": "select", "label": "Z Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "XVarTrans": {"type": "select", "label": "X Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "ZVarTrans": {"type": "select", "label": "Z Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Visual settings
    "ColorMapVar": {
        "type": "select",
        "label": "Color Mapping Variable",
        "options": ["XVar", "YVar", "ZVar"],
        "default": "ZVar",
    },
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "RangeColor": {
        "type": "text",
        "label": "Range Colors (JSON Array)",
        "default": '["red", "white", "blue"]',
    },
  },
  
  "Density": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": None},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    
    
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Visual settings
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "FillOpacity": {"type": "slider", "label": "Fill Opacity", "min": 0, "max": 1, "default": 0.5},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Density Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },
  
  "Donut": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["count", "mean", "sum", "median", "max", "min"],
        "default": "count",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Donut Chart"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },

  "Funnel": {
    # Data settings
    "CategoryVar": {"type": "text", "label": "Category Variable", "default": None},
    "ValuesVar": {"type": "text", "label": "Values Variable", "default": None},

    # Rendering settings
    
    "SeriesLabel": {"type": "text", "label": "Series Label", "default": "Funnel Data"},
    "SortStyle": {
        "type": "select",
        "label": "Sort Style",
        "options": ["ascending", "descending"],
        "default": "descending",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Funnel"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "Heatmap": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "MeasureVar": {"type": "select", "label": "Measure Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "MeasureVarTrans": {
        "type": "select",
        "label": "Measure Variable Transformation",
        "options": ["Identity", "Log", "SquareRoot", "Exp"],
        "default": "Identity",
    },

    # Rendering settings
    
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "LabelColor": {"type": "color", "label": "Label Color", "default": "#fff"},
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    "RangeColor": {
        "type": "text",
        "label": "Range Colors (JSON Array)",
        "default": '["#5b5b5b5d", "#00c4ff", "#9cff00"]',
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Heatmap Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "Histogram": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": None},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    
    

    # Histogram-specific settings
    "NumberBins": {"type": "slider", "label": "Number of Bins", "min": 1, "max": 100, "default": 20},
    "CategoryGap": {"type": "text", "label": "Category Gap", "default": "10%"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Histogram"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },

  "Line": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    
    
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "SmoothLine": {"type": "checkbox", "label": "Smooth Line", "default": True},
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Line Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },
  
  "Parallel": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": 15000},
    "Vars": {"type": "text", "label": "Variables", "default": None},
    "VarsTrans": {"type": "text", "label": "Variables Transformation", "default": None},

    # Rendering settings
    
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "Opacity": {"type": "slider", "label": "Line Opacity", "min": 0, "max": 1, "default": 0.05},
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 0.1, "max": 5, "default": 0.20},
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Parallel Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},
  },
  
  "Pie": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["count", "mean", "sum", "median", "max", "min"],
        "default": "count",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Pie Chart"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },

  "Radar": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "LabelColor": {"type": "color", "label": "Label Color", "default": "#fff"},
    "LineColors": {
        "type": "text",
        "label": "Line Colors (JSON Array)",
        "default": '["#213f7f", "#00a6fb", "#22c0df", "#8e5fa8", "#ed1690"]',
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Radar Chart"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "River": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVars": {"type": "text", "label": "Y Variables (JSON Array)", "default": None},
    "DateVar": {"type": "text", "label": "Date Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["sum", "mean", "median", "max", "min"],
        "default": "sum",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "River Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },

  "Rosetype": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["count", "mean", "sum", "median", "max", "min"],
        "default": "count",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Type": {
        "type": "select",
        "label": "Rosetype Type",
        "options": ["radius", "area"],
        "default": "radius",
    },
    "Radius": {"type": "text", "label": "Radius", "default": "55%"},
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Rosetype Chart"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "Scatter": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": 15000},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    
    
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "XVarTrans": {"type": "select", "label": "X Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Scatter Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },
  
  "Scatter3D": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": 15000},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "ZVar": {"type": "select", "label": "Z Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "XVarTrans": {"type": "select", "label": "X Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},
    "ZVarTrans": {"type": "select", "label": "Z Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "ColorMapVar": {
        "type": "select",
        "label": "Color Map Variable",
        "options": ["XVar", "YVar", "ZVar"],
        "default": "ZVar",
    },
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    "RangeColor": {
        "type": "text",
        "label": "Range Colors (JSON Array)",
        "default": '["red", "white", "blue"]',
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},
  },
  
  "StackedArea": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "Opacity": {"type": "slider", "label": "Area Opacity", "min": 0, "max": 1, "default": 0.5},
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Stacked Area"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "StackedBar": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Stacked Bar"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "StackedLine": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "SmoothLine": {"type": "checkbox", "label": "Smooth Line", "default": True},
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Stacked Line"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "StackedStep": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Line Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},
  },
  
  "Step": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "PreAgg": {"type": "checkbox", "label": "Pre-Aggregated Data", "default": False},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},
    "XVar": {"type": "select", "label": "X Variable", "default": None},
    "GroupVar": {"type": "select", "label": "Group Variable", "default": None},
    "FacetRows": {"type": "select", "label": "Facet Rows",  "options": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], "default": 1},
    "FacetCols": {"type": "select", "label": "Facet Columns", "options": [1,2,3,4], "default": 1},
    
    
    "AggMethod": {
        "type": "select",
        "label": "Aggregation Method",
        "options": ["mean", "sum", "median", "max", "min"],
        "default": "mean",
    },
    "YVarTrans": {"type": "select", "label": "Y Var Transformation", "options": ["None", "log", "logmin", "sqrt", "asinh", "perc_rank"], "default": "None"},

    # Rendering settings
    
    "LineWidth": {"type": "slider", "label": "Line Width", "min": 1, "max": 10, "default": 2},
    "SymbolSize": {"type": "slider", "label": "Symbol Size", "min": 1, "max": 20, "default": 6},
    "ShowLabels": {"type": "checkbox", "label": "Show Labels", "default": False},
    "LabelPosition": {
        "type": "select",
        "label": "Label Position",
        "options": ["top", "left", "right", "bottom", "inside"],
        "default": "top",
    },
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Interaction settings
    "ToolBox": {"type": "checkbox", "label": "Enable Toolbox", "default": True},
    "Brush": {"type": "checkbox", "label": "Enable Brush", "default": True},
    

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Line Plot"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},

    # Axis settings
    "AxisPointerType": {
        "type": "select",
        "label": "Axis Pointer Type",
        "options": ["line", "shadow", "cross", "none"],
        "default": "cross",
    },
    "YAxisTitle": {"type": "text", "label": "Y Axis Title", "default": None},
    "YAxisNameLocation": {
        "type": "select",
        "label": "Y Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "YAxisNameGap": {"type": "slider", "label": "Y Axis Name Gap", "min": 0, "max": 100, "default": 70},
    "XAxisTitle": {"type": "text", "label": "X Axis Title", "default": None},
    "XAxisNameLocation": {
        "type": "select",
        "label": "X Axis Name Location",
        "options": ["start", "middle", "end"],
        "default": "middle",
    },
    "XAxisNameGap": {"type": "slider", "label": "X Axis Name Gap", "min": 0, "max": 100, "default": 42},

    # Legend settings
    "Legend": {"type": "select", "label": "Show Legend", "options": [None, 'right', 'top'], "default": 'top'},
    "LegendPosRight": {"type": "text", "label": "Legend Position Right", "default": "0%"},
    "LegendPosTop": {"type": "text", "label": "Legend Position Top", "default": "5%"},
    "LegendBorderSize": {"type": "slider", "label": "Legend Border Size", "min": 0, "max": 5, "default": 0.25},
    "LegendTextColor": {"type": "select", "label": "Legend Text Color", "options": ["white", "gray","black"], "default": "gray"},

    # Reference lines
    
    
    

  },
  
  "WordCloud": {
    # Data settings
    "dt": {"type": "file", "label": "Data Table", "default": None},
    "SampleSize": {"type": "slider", "label": "Sample Size", "min": 1, "max": 100000, "default": None},
    "YVar": {"type": "select", "label": "Y Variable", "default": None},

    # Rendering settings
    
    "Theme": {
        "type": "select",
        "label": "Theme",
        "options": ['chalk', 'dark', 'essos', 'halloween', 'infographic', 'light', 'macarons', 'purple-passion', 'roma', 'romantic', 'shine', 'vintage', 'walden', 'westeros', 'white', 'wonderland'],
        "default": "dark",
    },
    
    "Width": {"type": "text", "label": "Chart Width", "default": "1250px"},
    "Height": {"type": "text", "label": "Chart Height", "default": "750px"},

    # Title and subtitle settings
    "Title": {"type": "text", "label": "Title", "default": "Word Cloud"},
    "TitleColor": {"type": "select", "label": "Title Color", "options": ["white", "gray","black"], "default": "gray"},
    "TitleFontSize": {"type": "slider", "label": "Title Font Size", "min": 10, "max": 50, "default": 20},
    "SubTitle": {"type": "text", "label": "Subtitle", "default": None},
    "SubTitleColor": {"type": "select", "label": "Subtitle Color", "options": ["white", "gray","black"], "default": "gray"},
    "SubTitleFontSize": {"type": "slider", "label": "Subtitle Font Size", "min": 10, "max": 30, "default": 12},
  }
}