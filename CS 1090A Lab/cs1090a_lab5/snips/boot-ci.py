# SOLUTION
# Initialize an empty list to store statistics for each feature
stats_list = []

feature_names_final = X_train.columns

# Loop through each feature to compute its bootstrapped statistics
for i in range(len(feature_names_final)):
    
    # Extracting the bootstrapped coefficient values for the current feature
    betavals = boot_betas_df.iloc[:, i]
    
    # Sorting the coefficient values to aid in percentile calculation
    betavals.values.sort()
    
    # Calculating the 2.5th percentile - lower bound of the 95% CI
    # your code here
    x1 = np.round(np.percentile(betavals, ...), 2)
    
    # Calculating the 97.5th percentile - upper bound of the 95% CI
    x2 = np.round(np.percentile(betavals, ...), 2)
    
    # Calculating mean and standard deviation of the bootstrapped coefficients
    mean = np.round(np.mean(betavals),2)
    std = np.round(np.std(betavals),2)
    
    # Appending computed statistics for current feature to the stats_list
    stats_list.append([feature_names_final[i], mean, std, x1, x2])

# Convert the stats_list into a dataframe for easy visualization and analysis
boot_beta_df = pd.DataFrame(stats_list, columns=['feature', 'boot_mean', 'boot_std', '95_low', '95_high'])

# Display the final dataframe with bootstrapped statistics and confidence intervals
boot_beta_df