# QuickEcharts

<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Logo.PNG" align="center" width="800" />

Create Echart plots in a single simple function call, with internal data wrangling via polars

This package is in the early stages. The idea is to design it in a similar way to my R package AutoPlots. The goal is to make plotting echarts quick and easy and to allow polars to do the heavy data wrangling work under the hood.


### Histograms

```python
# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Histogram as h

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
data = pl.read_csv(FilePath)

# Create Histogram Plot in Jupyter Lab
p1 = h.Histogram(
  Notebook = 'jupyter_lab',
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = None,
  YVarTrans = "sqrt",
  Title = 'Histogram Plot',
  XAxisTitle = 'Daily Liters Buckets',
  Theme = 'wonderland',
  NumberBins = 20,
  CategoryGap = "10%",
  HorizonalLine = 500,
  HorizonalLineName = 'Yaxis Value')

# Needed to display
p1.load_javascript()

# In a new cell
p1.render_notebook()
```

#### Jupyter Lab View
<img src="https://github.com/AdrianAntico/QuickEcharts/blob/main/QuickEcharts/Images/Histogram.PNG" align="center" width="800" />
