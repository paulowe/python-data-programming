import pandas as pd

# DPP. Detect null/missing data




# Print Indices, given a series
def print_pd_index():
   pdSeries = pd.Series([4, 7, -5, 3], index=['a','b','c','d'])
   print(pdSeries.index)