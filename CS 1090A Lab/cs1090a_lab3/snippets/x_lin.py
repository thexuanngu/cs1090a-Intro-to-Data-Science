# create a range of values to predict on
x_lin = np.linspace(x.min(), x.max(), 1000)

# If the model was fit on data with a names for the predictor(s)
# (e.g., a Series or DataFrame)
# and is then asked to predict on data with no names
# (e.g., a numpy array)
# it will complain!
# These warnings are harmless but ugly :(
# One way to get it to shush is to turn the data into a type
# that does include a name for the predictor(s)
x_lin = pd.DataFrame(x_lin, columns=['temp'])
x_lin.head()