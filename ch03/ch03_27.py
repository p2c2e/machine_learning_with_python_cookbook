# Attempt to replace values with NaN
dataframe['Sex'] = dataframe['Sex'].replace('male', NaN)