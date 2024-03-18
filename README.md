# QuickEcharts

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Logo.PNG" align="center" width="800" />

Plot Echarts quickly, with a simple API, and to allow polars to do the data wrangling under the hood, saving you valuable time.

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

## Box Plot

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
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = None,
  FacetRows = 1,
  FacetCols = 1,
  FacetLevels = None,
  YVarTrans = "sqrt",
  RenderHTML = False,
  Theme = 'wonderland',
  Title = 'Histogram',
  TitleColor = "#fff",
  TitleFontSize = 20,
  SubTitle = None,
  SubTitleColor = "#fff",
  SubTitleFontSize = 12,
  XAxisTitle = 'Daily Liters Buckets',
  XAxisNameLocation = 'middle',
  XAxisNameGap = 42,
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
