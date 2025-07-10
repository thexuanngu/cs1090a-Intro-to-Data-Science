# range of candidate k values
ks = range(1, 101)
# lists to store train and test MSEs
train_mses = []
test_mses = []
# fit a model for each k and record MSEs
for k in ks:
    cur_knn = KNeighborsRegressor(n_neighbors=k).fit(x_train, y_train)
    train_mses.append(mean_squared_error(y_train, cur_knn.predict(x_train)))
    test_mses.append(mean_squared_error(y_test, cur_knn.predict(x_test)))