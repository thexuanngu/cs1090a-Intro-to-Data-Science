y_hat_train = lr.predict(x_train)
((y_train - y_hat_train)**2).mean()