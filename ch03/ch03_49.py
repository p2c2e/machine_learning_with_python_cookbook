# Group by month, count rows
dataframe.resample('M', label='left').count()