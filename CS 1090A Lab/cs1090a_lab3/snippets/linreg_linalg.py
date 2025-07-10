betas = np.linalg.inv(X.T@X)@X.T@y_train
betas