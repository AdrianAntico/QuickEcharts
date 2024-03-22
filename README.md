# QuickEcharts

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Logo.PNG" align="center" width="800" />

QuickEcharts is a Python package that enables one to plot Echarts quickly. It piggybacks off of the pyecharts package that pipes into Apache Echarts. Pyecharts is a great package for fully customizing plots but is quite a challenge to make use of quickly. QuickEcharts solves this with a simple API for defining plotting elements and data, along with automatic data wrangling operations, using polars, to prepare the data properly and fast.

# Installation
```
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
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
data = pl.read_csv(FilePath)

p1 = Charts.Area(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  GradientColor1 = '#c812ca',
  GradientColor2 = '#123fed0d',
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Area.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  GradientColor1 = '#c812ca',
  GradientColor2 = '#123fed0d',
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Area_GroupVar.PNG" align="center" width="800" />

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  GradientColor1 = '#c812ca',
  GradientColor2 = '#123fed0d',
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Area_Facet.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = None,
  FacetCols = 1,
  FacetRows = 1,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Bar Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Bar.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetCols = 1,
  FacetRows = 1,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Bar Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Bar_GroupVar.PNG" align="center" width="800" />



```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Bar(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  XVar = 'Date',
  GroupVar = 'Brand',
  FacetCols = 2,
  FacetRows = 2,
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Bar Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Bar_Facet.PNG" align="center" width="800" />

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

# Get data
import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Build Plot
p1 = Charts.Bar3D(
  dt = data,
  PreAgg = False,
  YVar = 'Brand',
  XVar = 'Category',
  ZVar = 'Daily Liters',
  AggMethod = 'mean',
  ZVarTrans = "logmin",
  RenderHTML = False,
  Title = 'Bar3D Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  ToolBox = True,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  Brush = True,
  DataZoom = True,
  Theme = 'wonderland')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Bar3D.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.BoxPlot(
  dt = data,
  SampleSize = 100000,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  YVarTrans = "logmin",
  FlipAxis = False,
  RenderHTML = False,
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
  Theme = 'wonderland',
  Legend = None,
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Boxplot.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create plot
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = None,
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  AggMethod = 'mean',
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 2,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Copula Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 10,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

c.load_javascript()
c.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Copula.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create plot
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  AggMethod = 'mean',
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 2,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Copula Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 10,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

c.load_javascript()
c.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Copula_GroupVar.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create plot
p1 = Charts.Copula(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  AggMethod = 'mean',
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 2,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Copula Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 10,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

c.load_javascript()
c.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Copula_Facet.PNG" align="center" width="800" />

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

# Get data
import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Build Plot
p1 = Charts.Copula3D(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  ZVar = 'Daily Margin',
  ColorMapVar = "ZVar",
  AggMethod = 'mean',
  RenderHTML = False,
  SymbolSize = 6)

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Copula3D.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Density(
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = None,
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  YVarTrans = "sqrt",
  LineWidth = 1,
  FillOpacity = 0.75,
  RenderHTML = False,
  Title = 'Density Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  XAxisTitle = 'Daily Liters Buckets',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'macarons',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = 35,
  VerticalLineName = "Xaxis Value",
  HorizontalLine = 45000,
  HorizontalLineName = 'Yaxis Value')

# Needed to display
p1.load_javascript()
p1.render_notebook()

```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Density.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  YVarTrans = "sqrt",
  LineWidth = 1,
  FillOpacity = 0.75,
  RenderHTML = False,
  Title = 'Density Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  XAxisTitle = 'Daily Liters Buckets',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'macarons',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = 35,
  VerticalLineName = "Xaxis Value",
  HorizontalLine = 45000,
  HorizontalLineName = 'Yaxis Value')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Density_Facet.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  Title = 'Donut Chart',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Theme = 'wonderland',
  Legend = None,
  LegendPosRight = '0%',
  LegendPosTop = '5%')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Donut.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Funnel(
  dt = data,
  CategoryVar = ['Daily Units', 'Daily Revenue', 'Daily Margin', 'Daily Liters'],
  ValuesVar = [100, 80, 60, 40],
  SeriesLabel = "Funnel Data",
  SortStyle = 'decending',
  Theme = 'wonderland',
  Title = "Funnel Plot",
  TitleColor = "#fff",
  TitleFontSize = 40,
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  RenderHTML = False)

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Funnel_Descending.PNG" align="center" width="800" />

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Funnel(
  dt = data,
  CategoryVar = ['Daily Units', 'Daily Revenue', 'Daily Margin', 'Daily Liters'],
  ValuesVar = [100, 80, 60, 40],
  SeriesLabel = "Funnel Data",
  SortStyle = 'ascending',
  Theme = 'wonderland',
  Title = "Funnel Plot",
  TitleColor = "#fff",
  TitleFontSize = 40,
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  RenderHTML = False)

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Funnel_Ascending.PNG" align="center" width="800" />


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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Heatmap(
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
  Title = 'Heatmap',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  AxisPointerType = 'cross',
  YAxisTitle = 'Brand',
  YAxisNameLocation = 'end',
  YAxisNameGap = 10,
  XAxisTitle = 'Category',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'purple-passion',
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True)

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Heatmap.PNG" align="center" width="800" />

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
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Histogram(
  dt = data,
   SampleSize = 500000,
   YVar = 'Daily Liters',
   GroupVar = None,
   FacetRows = 1,
   FacetCols = 1,
   FacetLevels = None,
   YVarTrans = None,
   NumberBins = 20,
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
   CategoryGap = "10%",
   Theme = 'wonderland',
   BackgroundColor = "#000",
   Width = None,
   Height = None,
   Legend = 'top',
   LegendPosRight = '0%',
   LegendPosTop = '5%',
   LegendBorderSize = 1,
   LegendTextColor = "#fff",
   ToolBox = True,
   Brush = True,
   DataZoom = True,
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
   AnimationDelayUpdate = 0,
   RenderHTML = False)

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Histogram(
  Notebook = 'jupyter_lab',
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  YVarTrans = "sqrt",
  Title = 'Histogram',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  XAxisTitle = 'Daily Liters Buckets',
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
  HorizonalLine = 500,
  HorizonalLineName = 'Yaxis Value')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram_Facet.PNG" align="center" width="800" />

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
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  SmoothLine = True,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Line_MultiYVar.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  SmoothLine = True,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Line_GroupVar.PNG" align="center" width="800" />

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  SmoothLine = True,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Line_Facet.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Parallel(
  dt = data,
  SampleSize = 15000,
  Vars = ['Daily Liters', 'Daily Units', 'Daily Revenue', 'Daily Margin'],
  VarsTrans = ['logmin'] * 4,
  Theme = 'wonderland',
  RenderHTML = False,
  SymbolSize = 6,
  Opacity = 0.05,
  LineWidth = 0.20)

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Parallel.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Pie(
  dt = data,
  PreAgg = False,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  AggMethod = 'count',
  YVarTrans = "Identity",
  RenderHTML = False,
  Title = 'Pie Chart',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Theme = 'wonderland',
  Legend = None,
  LegendPosRight = '0%',
  LegendPosTop = '5%')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Pie.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Create Plot in Jupyter Lab
p1 = Charts.Radar(
  dt = data,
  YVar = 'Daily Liters',
  GroupVar = 'Brand',
  AggMethod = 'mean',
  YVarTrans = "Identity",
  RenderHTML = False,
  Title = 'Radar Chart',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Theme = 'wonderland',
  LabelColor = '#fff',
  LineColors = ["#213f7f", "#00a6fb", "#22c0df", "#8e5fa8", "#ed1690"],
  Legend = None,
  LegendPosRight = '0%',
  LegendPosTop = '5%')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Radar.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  Theme = 'wonderland',
  AxisPointerType = "cross",
  Title = "River Plot",
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '10%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  RenderHTML = False)

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/River_MultiYVar.PNG" align="center" width="800" />

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  Theme = 'wonderland',
  AxisPointerType = "cross",
  Title = "River Plot",
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Legend = 'top',
  LegendPosRight = '0%',
  LegendPosTop = '10%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  RenderHTML = False)

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/River_GroupVar.PNG" align="center" width="800" />

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
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  Type = "area",
  Radius = "55%",
  Title = 'Rosetype Chart',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  Theme = 'wonderland',
  Legend = None,
  LegendPosRight = '0%',
  LegendPosTop = '5%')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Rosetype.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  AggMethod = 'mean',
  YVarTrans = "Identity",
  XVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Scatter Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 5,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Scatter.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  AggMethod = 'mean',
  YVarTrans = "Identity",
  XVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Scatter Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 5,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Scatter_GroupVar.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

p1 = Charts.Scatter(
  dt = data,
  SampleSize = 15000,
  YVar = 'Daily Liters',
  XVar = 'Daily Units',
  GroupVar = 'Brand',
  FacetRows = 2,
  FacetCols = 2,
  FacetLevels = None,
  AggMethod = 'mean',
  YVarTrans = "Identity",
  XVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  SymbolSize = 6,
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Scatter Plot',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 5,
  AxisPointerType = 'cross',
  YAxisTitle = 'Daily Liters',
  YAxisNameLocation = 'end',
  YAxisNameGap = 15,
  XAxisTitle = 'Daily Units',
  XAxisNameLocation = 'end',
  XAxisNameGap = 10,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '5%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Scatter_Facet.PNG" align="center" width="800" />

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

# Get data
import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
data = pl.read_csv(FilePath)

# Build Plot
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
  SymbolSize = 6)

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Scatter3D.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/StackedArea.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/StackedBar.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
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
  XAxisTitle = 'Date',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/StackedLine.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Stacked Step',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/StackedStep.PNG" align="center" width="800" />

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
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Step Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Step_MultiYVar.PNG" align="center" width="800" />


```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Step Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Step_GroupVar.PNG" align="center" width="800" />

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Charts
from pyecharts.globals import CurrentConfig, NotebookType 
CurrentConfig.NOTEBOOK_TYPE = 'jupyter_lab'

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
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
  AggMethod = 'sum',
  YVarTrans = "Identity",
  RenderHTML = False,
  LineWidth = 2,
  Symbol = "emptyCircle",
  ShowLabels = False,
  LabelPosition = "top",
  Title = 'Step Plot',
  TitleColor = "#fff",
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
  Theme = 'wonderland',
  Legend = 'right',
  LegendPosRight = '0%',
  LegendPosTop = '15%',
  ToolBox = True,
  Brush = True,
  DataZoom = True,
  VerticalLine = None,
  VerticalLineName = 'Line Name',
  HorizontalLine = None,
  HorizontalLineName = 'Line Name')

# Needed to display
p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Step_Facet.PNG" align="center" width="800" />

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

import polars as pl
FilePath = "C:/Users/Bizon/Documents/GitHub/rappwd/FakeBevData.csv"
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

p1.load_javascript()
p1.render_notebook()
```

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Wordcloud.PNG" align="center" width="800" />

</details>
