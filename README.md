# QuickEcharts
Create Echart plots in a single simple function call, with internal data wrangling via polars

```python

# Environment
import pkg_resources
import polars as pl
from QuickEcharts import Histogram

# Pull Data from Package
FilePath = pkg_resources.resource_filename('QuickEcharts', 'datasets/FakeBevData.csv')
data = pl.read_csv(FilePath)

# Create Histogram Plot in Jupyter Lab
p1 = Histogram(
  Notebook = 'jupyter_lab',
  dt = data,
  SampleSize = 100000,
  YVar = "Daily Liters",
  GroupVar = None,
  YVarTrans = "sqrt",
  Title = 'Histogram Plot',
  Theme = 'wonderland',
  NumberBins = 20,
  CategoryGap = "10%",
  HorizonalLine = 500,
  HorizonalLineName = 'Yaxis Value')

# To display in jupyter lab
p1.load_javascript()
p1.render_notebook()
```
pip install git+https://github.com/AdrianAntico/QuickEcharts.git#egg=quickecharts
