# Group rows, calculate mean
dataframe.groupby(['Sex','Survived'])['Age'].mean()