# SOLUTION
# Configure number of bootstraps
n_boots = 1000

# Lists to save models and coefficients
boot_models = []
boot_betas = []

for i in range(n_boots):
   
    # Randomly sample indices with replacement to create bootstrap samples
    boot_i = np.random.choice(X_train.index, 
                              replace = True, 
                              size = len(X_train.index)) 

    # Create bootstrap datasets for features and target variable using the sampled indices
    X_train_boot = X_train.iloc[boot_i]
    y_train_boot = y_train.iloc[boot_i]
    
    # Train a linear regression model on the bootstrap sample
    boot_linreg = LinearRegression().fit(X_train_boot, y_train_boot)

    # Save the trained model
    boot_models.append(boot_linreg)
    
    # print(boot_linreg.intercept_[0], boot_linreg.coef_[0])

    # Extract and save coefficients from the trained model (including the intercept)
    coefs = np.insert(boot_linreg.coef_[0], 0, boot_linreg.intercept_[0], axis=None)
    boot_betas.append(coefs)