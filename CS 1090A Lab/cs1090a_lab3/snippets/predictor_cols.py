# Get a list of all columns excluding the response 'count'
cols = df.drop('count', axis=1).columns

# There are 10 features
# This is a nice even number for plotting in a grid with 2 columns
print(f"There are {len(cols)} potential predictors")