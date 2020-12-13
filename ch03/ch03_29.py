# Load data, set missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])