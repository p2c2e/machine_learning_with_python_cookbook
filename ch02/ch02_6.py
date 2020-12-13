# Load library
import pandas as pd

# Create URL
url = 'https://tinyurl.com/simulated_data'

# Load dataset
dataframe = pd.read_csv(url)

# View first two rows
dataframe.head(2)