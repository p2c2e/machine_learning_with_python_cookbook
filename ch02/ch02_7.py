# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/simulated_excel'

# Load data
dataframe = pd.read_excel(url, sheetname=0, header=1)

# View the first two rows
dataframe.head(2)