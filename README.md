# QuickEcharts

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Logo.PNG" align="center" width="800" />

QuickEcharts is in the early stages. The idea is to design it similar to my R package AutoPlots. The goal is to make plotting echarts quick, easy, and to allow polars to do the data wrangling under the hood, saving the end user valuable time.

# Installation
```
pip install git+https://github.com/AdrianAntico/QuickEcharts.git#egg=quickecharts
```

<br>

# Code Examples

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

# Create BoxPlot in Jupyter Lab
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

#### Jupyter Lab View
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

# Create Histogram Plot in Jupyter Lab
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
  Title = 'Histogram Plot',
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
#### Jupyter Lab View
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

# Create Histogram Plot in Jupyter Lab
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
  Title = 'Histogram Plot',
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

#### Jupyter Lab View
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

# Create RoseType Chart Plot in Jupyter Lab
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

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Donut.PNG" align="center" width="800" />

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

# Create Histogram Plot in Jupyter Lab
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

#### Jupyter Lab View
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

# Create Histogram Plot in Jupyter Lab
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

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram_Facet.PNG" align="center" width="800" />

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

# Create Pie Chart in Jupyter Lab
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

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Pie.PNG" align="center" width="800" />

</details>

<br>

## Radar Chart

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

#### Jupyter Lab View
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

# Create RoseType Chart Plot in Jupyter Lab
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

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Rosetype.PNG" align="center" width="800" />

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

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Wordcloud.PNG" align="center" width="800" />

</details>
