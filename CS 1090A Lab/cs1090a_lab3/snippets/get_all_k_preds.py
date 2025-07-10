# 'fit' a model for each k and collect the predictions
all_preds = []
for k in ks:
    preds = KNeighborsRegressor(n_neighbors=k).fit(x_train, y_train).predict(x_lin)
    all_preds.append(preds)