# SOLUTION
# K-Fold cross-validation

# Number of partitions/folds to divide the dataset into
k_folds = 8

# Calculate the size of each fold. If the dataset's length isn't 
# perfectly divisible by k, some folds might have an extra data point.
fold_size = len(design_train_df) // k_folds

# This list will store the mean squared error for each fold.
val_mses = []

# Why might we want to shuffle our data first?
X_train = design_train_df.sample(frac=1, replace=False, random_state=42).copy() # frac=1 effectively shuffles
y_train = y_train.iloc[X_train.index] # sort y by indices of shuffled X
X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

# Iterate over each fold
for i in range(k_folds):

    # Compute the starting and ending indices for the test set based on the current fold.
    # For example, if fold_size is 100:
    # i=0 -> start=0, end=100
    # i=1 -> start=100, end=200
    # ... and so on
    start, end = i * fold_size, (i + 1) * fold_size

    # Use slicing to get the test set for the current fold from the main dataset.
    # your code here
    X_val_fold = X_train[...]
    y_val_fold = ...

    # For the training set, we take all data EXCEPT the test fold. This is achieved
    # by concatenating the two slices of data that are before and after the test fold.
    # Note: we are using `pd.concat` for DataFrames instead of `np.concatenate`.
    X_train_folds = pd.concat([X_train[:start], X_train[end:]])
    y_train_folds = np.concatenate([y_train[:start], y_train[end:]])

    # Initialize a linear regression model
    model = LinearRegression()
    
    # Train the model using the training set
    # your code here
    model.fit(..., ...)
    
    # Predict the target values for the validation set
    # your code here
    y_hat_val_fold = model.predict(...)

    # Compute the mean squared error for the current fold's predictions
    # your code here
    mse = mean_squared_error(...)

    # Store the computed MSE to our list
    val_mses.append(mse)

# Calculate the average mean squared error across all folds.
avg_mse = np.mean(val_mses)

# Print the result
print(f"Average MSE from simplified scratch implementation: {avg_mse:.2f}")
