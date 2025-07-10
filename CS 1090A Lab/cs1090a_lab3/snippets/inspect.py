import pandas as pd
# load the data
df = pd.read_csv('data/bikeshare.csv')
# various ways of quick inspection
print("df.head()")
display(df.head())
print("df.info()")
display(df.info())
print("df.describe()")
display(df.describe())