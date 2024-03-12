# QuickEcharts

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Logo.PNG" align="center" width="800" />

Create Echarts plots in a single simple function call, with internal data wrangling via polars

This package is in the early stages. The idea is to design it in a similar way to my R package AutoPlots. The goal is to make plotting echarts quick and easy and to allow polars to do the heavy data wrangling work under the hood.

### Installation
```
pip install git+https://github.com/AdrianAntico/QuickEcharts.git#egg=quickecharts
```


### Histogram

<details><summary>Click for code</summary>

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

# In a new cell
p1.render_notebook()
```

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram.PNG" align="center" width="800" />

</details>

### Histogram Facet

<details><summary>Click for code</summary>

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

# In a new cell
p1.render_notebook()
```

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram_Facet.PNG" align="center" width="800" />

</details>

### Density

<details><summary>Click for code</summary>

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
  Theme = 'macarons',
  NumberBins = 20,
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

# In a new cell
p1.render_notebook()

```
#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Density.PNG" align="center" width="800" />
</details>

### Density Facet

<details><summary>Click for code</summary>

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
  Theme = 'macarons',
  NumberBins = 20,
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

# In a new cell
p1.render_notebook()
```

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Density_Facet.PNG" align="center" width="800" />
</details>
