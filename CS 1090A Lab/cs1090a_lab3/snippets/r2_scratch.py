total_var = sum((y_test.mean() - y_test)**2)
unexp_var = sum((y_test - y_hat_test)**2)
1 - (unexp_var/total_var)