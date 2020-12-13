# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/simulated_json'

# Load data
dataframe = pd.read_json(url, orient='columns')

# View the first two rows
dataframe.head(2)