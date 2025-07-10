# SOLUTION
import statsmodels.api as sm
from statsmodels.api import OLS

# your code here
X_train = sm.add_constant(...)
ols = OLS(y_train, np.array(X_train))
results = ols.fit()
# get the parameters
results.params 