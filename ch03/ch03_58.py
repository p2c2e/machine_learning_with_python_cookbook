# Merge DataFrames
pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer')