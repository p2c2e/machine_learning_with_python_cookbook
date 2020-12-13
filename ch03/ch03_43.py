# Group rows, count rows
dataframe.groupby('Survived')['Name'].count()