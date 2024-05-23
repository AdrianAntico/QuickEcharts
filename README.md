# QuickEcharts

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Logo.PNG)

QuickEcharts is a Python package that enables one to plot Echarts quickly. It piggybacks off of the pyecharts package that pipes into Apache Echarts. Pyecharts is a great package for fully customizing plots but is quite a challenge to make use of quickly. QuickEcharts solves this with a simple API for defining plotting elements and data, along with automatic data wrangling operations, using polars, to correctly structure data fast.

For the Code Examples below, there is a dataset in the QuickEcharts/datasets folder named FakeBevData.csv that you can download for replication purposes.

# Installation
```
pip install QuickEcharts

or 

pip install git+https://github.com/AdrianAntico/QuickEcharts.git#egg=quickecharts
```

<br>

# Code Examples

<br>

## Area

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Area(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  Opacity = 0.5,
  GradientColor1 = '#e12191',
  GradientColor2 = '#0926800d',
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Area Plot',
  TitleColor = "lightgray",
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
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Area.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Area(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  Opacity = 0.5,
  GradientColor1 = '#c86589',
  GradientColor2 = '#06a7ff0d',
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Area_GroupVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Area(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  Opacity = 0.5,
  GradientColor1 = '#c86589',
  GradientColor2 = '#06a7ff0d',
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Area_Facet.PNG)


</details>

<br>

## Bar

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = None,
  FacetCols = 1,
  FacetRows = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Bar Plot',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'middle',
  YAxisNameGap = 70,
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 1,
  LegendTextColor = "#lightgray",
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Bar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetCols = 1,
  FacetRows = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Bar_GroupVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetCols = 2,
  FacetRows = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Bar_Facet.PNG)

</details>


<br>


## Bar3D

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Bar3D(
  dt = data,
  PreAgg = False,
  YVar = 'Brand',
  XVar = 'Category',
  ZVar = 'Daily Liters',
  AggMethod = 'mean',
  ZVarTrans = "logmin",
  RenderHTML = False,
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
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Bar3D.PNG)

</details>


<br>



## Box

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.BoxPlot(
  dt = data,
  SampleSize = 100000,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  YVarTrans = "logmin",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Box Plot',
  TitleColor = "lightgray",
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
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
  HorizontalLine = None,
  HorizontalLineName = 'Line Name',
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Boxplot.PNG)

</details>


<br>

## Copula

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = None,
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Copula Plot',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'middle',
  YAxisNameGap = 70,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Copula.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Copula_GroupVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Copula_Facet.PNG)

</details>


<br>


## Copula3D

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Copula3D(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  ZVar = 'Daily Margin',
  ColorMapVar = "ZVar",
  AggMethod = 'mean',
  RenderHTML = False,
  RangeColor = ["red", "white", "blue"],
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Copula3D.PNG)

</details>


<br>

## Density

<details><summary>Click for code example</summary>

```python

# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Density(
  dt = data,
  SampleSize = 500000,
  YVar = "Daily Liters",
  GroupVar = None,
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  YVarTrans = "sqrt",
  RenderHTML = False,
  LineWidth = 2,
  FillOpacity = 0.5,
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Density Plot',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  XAxisTitle = 'Daily Liters',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  VerticalLine = 5,
  VerticalLineName = 'Line Name',
  HorizontalLine = 225000,
  HorizontalLineName = 'Line Name',
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()

```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Density.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Density(
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  YVarTrans = "sqrt",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Density_Facet.PNG)

</details>

<br>

## Donut

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Donut(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  AggMethod = 'count',
  YVarTrans = "Identity",
  RenderHTML = False,
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = 'Donut Chart',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'right',
  LegendPosRight = '5%',
  LegendPosTop = '5%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Donut.PNG)

</details>


<br>

## Funnel

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Funnel(
  dt = data,
  CategoryVar = ['Daily Units', 'Daily Revenue', 'Daily Margin', 'Daily Liters'],
  ValuesVar = [100, 80, 60, 40],
  RenderHTML = False,
  SeriesLabel = "Funnel Data",
  SortStyle = 'descending',
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = "Funnel",
  TitleColor = "lightgray",
  TitleFontSize = 20,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Funnel_Descending.PNG)

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Funnel(
  dt = data,
  CategoryVar = ['Daily Units', 'Daily Revenue', 'Daily Margin', 'Daily Liters'],
  ValuesVar = [100, 80, 60, 40],
  RenderHTML = False,
  SeriesLabel = "Funnel Data",
  SortStyle = 'ascending',
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = "Funnel",
  TitleColor = "lightgray",
  TitleFontSize = 20,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Funnel_Ascending.PNG)


</details>


<br>



## Heatmap

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Heatmap(
  dt = data,
  PreAgg = False,
  YVar = 'Brand',
  XVar = 'Category',
  MeasureVar = 'Daily Liters',
  AggMethod = 'mean',
  MeasureVarTrans = "Identity",
  RenderHTML = False,
  ShowLabels = False,
  LabelPosition = "top",
  LabelColor = "#fff",
  Theme = 'dark',
  RangeColor = ["#5b5b5b5d", "#00c4ff", "#9cff00"],
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Heatmap',
  TitleColor = "lightgray",
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
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Heatmap.PNG)

</details>


<br>


## Histogram

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Histogram(
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = None,
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  YVarTrans = "logmin",
  RenderHTML = True,
  Theme = 'dark',
  CategoryGap = "0%",
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Histogram',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  XAxisTitle = "Horray",
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  VerticalLine = 10,
  VerticalLineName = 'Line Name',
  HorizontalLine = 40000,
  HorizontalLineName = 'Line Name',
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "elasticOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Histogram.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Histogram(
  dt = data,
  SampleSize = 500000,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  YVarTrans = None,
  RenderHTML = False
  NumberBins = 20,
  CategoryGap = "10%",
  Theme = 'wonderland',
  BackgroundColor = "#000",
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
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Histogram_Facet.PNG)

</details>

<br>


## Line

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Line(
  dt = data,
  PreAgg = False,
  YVar = ['Daily Liters', 'Daily Margin', 'Daily Revenue', 'Daily Units'],
  XVar = 'Date',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  SmoothLine = True,
  LineWidth = 2,
  Symbol = None,
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Line Plot',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  YAxisTitle = None,
  YAxisNameLocation = 'middle',
  YAxisNameGap = 70,
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'right',
  LegendPosRight = '5%',
  LegendPosTop = '15%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Line_MultiYVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Line(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Line_GroupVar.PNG)

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Line(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Line_Facet.PNG)

</details>


<br>

## Parallel

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Parallel(
  dt = data,
  SampleSize = 15000,
  Vars = ['Daily Liters', 'Daily Units', 'Daily Revenue', 'Daily Margin'],
  VarsTrans = ['logmin'] * 4,
  RenderHTML = False,
  SymbolSize = 6,
  Opacity = 0.05,
  LineWidth = 0.20,
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = 'Parallel Plot',
  TitleColor = "lightgray",
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Parallel.PNG)

</details>

<br>


## Pie

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Pie(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  AggMethod = 'count',
  YVarTrans = None,
  RenderHTML = False,
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = 'Pie Chart',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = "right",
  LegendPosRight = '5%',
  LegendPosTop = '5%',
  LegendBorderSize = 0.25,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Pie.PNG)

</details>

<br>

## Radar

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Radar(
  dt = data,
  YVar = ['Daily Liters', 'Daily Margin'],
  GroupVar = 'Brand',
  AggMethod = 'mean',
  YVarTrans = None,
  RenderHTML = True,
  LabelColor = '#fff',
  LineColors = ["#ed1690", "#8e5fa8", "#00a6fb", "#213f7f", "#22c0df"],
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = 'Radar Chart',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'right',
  LegendPosRight = '2%',
  LegendPosTop = '5%',
  LegendBorderSize = 0.25,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Radar.PNG)

</details>

<br>


## River

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.River(
  dt = data,
  PreAgg = False,
  YVars = ['Daily Liters', 'Daily Units', 'Daily Revenue', 'Daily Margin'],
  DateVar = 'Date',
  GroupVar = None,
  AggMethod = "sum",
  YVarTrans = None,
  RenderHTML = False,
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  AxisPointerType = "cross",
  Title = "River Plot",
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'right',
  LegendPosRight = '5%',
  LegendPosTop = '15%',
  LegendBorderSize = 0.25,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/River_MultiYVar.PNG)

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.River(
  dt = data,
  PreAgg = False,
  YVars = 'Daily Liters',
  DateVar = 'Date',
  GroupVar = 'Brand',
  AggMethod = "sum",
  YVarTrans = None,
  RenderHTML = False,
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
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/River_GroupVar.PNG)

</details>

<br>


## Rosetype

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Rosetype(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  AggMethod = 'count',
  YVarTrans = "Identity",
  RenderHTML = False,
  Type = "radius",
  Radius = "55%",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  Title = 'Rosetype Chart',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'right',
  LegendPosRight = '5%',
  LegendPosTop = '5%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Rosetype.PNG)

</details>


<br>


## Scatter

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  YVarTrans = "logmin",
  XVarTrans = "logmin",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Scatter Plot',
  TitleColor = "lightgray",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'middle',
  YAxisNameGap = 70,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '2%',
  LegendBorderSize = 1,
  LegendTextColor = "lightgray",
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Scatter.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  YVarTrans = "Identity",
  XVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Scatter_GroupVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'mean',
  YVarTrans = "Identity",
  XVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Scatter_Facet.PNG)

</details>


<br>


## Scatter3D

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Scatter3D(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  ZVar = 'Daily Margin',
  ColorMapVar = "ZVar",
  AggMethod = 'mean',
  YVarTrans = "logmin",
  XVarTrans = "logmin",
  ZVarTrans = "logmin",
  RenderHTML = False,
  SymbolSize = 6,
  Theme = 'dark',
  RangeColor = ["red", "white", "blue"],
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Scatter3D.PNG)

</details>


<br>


## Stacked Area

<details><summary>Click for code example</summary>

```python
# Environment
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.StackedArea(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  Opacity = 0.5,
  LineWidth = 2,
  Symbol = None,
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Theme = 'dark',
  BackgroundColor = None,
  Width = "1200px",
  Height = "750px",
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  Title = 'Stacked Area',
  TitleColor = "lightgray",
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
  Legend = "right",
  LegendPosRight = '2%',
  LegendPosTop = '10%',
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/StackedArea.PNG)

</details>


<br>


## Stacked Bar

<details><summary>Click for code example</summary>

```python
# Environment
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.StackedBar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/StackedBar.PNG)

</details>


<br>



## Stacked Line

<details><summary>Click for code example</summary>

```python
# Environment
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.StackedLine(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/StackedLine.PNG)

</details>

<br>



## Stacked Step

<details><summary>Click for code example</summary>

```python
# Environment
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.StackedStep(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
  LegendTextColor = "#fff",
  AnimationThreshold = 2000,
  AnimationDuration = 1000,
  AnimationEasing = "cubicOut",
  AnimationDelay = 0,
  AnimationDurationUpdate = 300,
  AnimationEasingUpdate = "cubicOut",
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/StackedStep.PNG)

</details>

<br>


## Step

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Step(
  dt = data,
  PreAgg = False,
  YVar = ['Daily Liters', 'Daily Margin', 'Daily Revenue', 'Daily Units'],
  XVar = 'Date',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Step_MultiYVar.PNG)


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Step(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Step_GroupVar.PNG)

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Step(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  TimeLine = False,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
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
  LegendBorderSize = 1,
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
  AnimationDelayUpdate = 0)

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Step_Facet.PNG)

</details>


<br>


## Word Cloud

<details><summary>Click for code example</summary>

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "..FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.WordCloud(
  dt = data,
  SampleSize = 100000,
  YVar = 'Brand',
  RenderHTML = False,
  SymbolType = 'diamond',
  Title = 'Word Cloud',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Theme = 'wonderland')

# Needed to display
p1.load_javascript()

# In new cell
p1.render_notebook()
```

![](https://github.com/AdrianAntico/QuickEcharts/raw/main/QuickEcharts/Images/Wordcloud.PNG)

</details>
