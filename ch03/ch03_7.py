# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com//titanic-csv'

# Load data
dataframe = pd.read_csv(url)

# Select first row
dataframe.iloc[0]