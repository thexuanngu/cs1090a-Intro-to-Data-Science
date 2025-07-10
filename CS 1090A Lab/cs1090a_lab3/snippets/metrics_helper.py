def get_metrics(model, name: str, data: tuple) -> dict:
    '''
    Parameters
    ----------
    model : (sklearn estimator) This is your fitted sklearn model
    name : (str) A name to represent your model
    data : (tuple) contains train and test split for x and y

    Returns:
    metrics : (dict) should have entries for:
             name, train_mse, test_mse, r2_train, and r2_test
    '''
    x_train, x_test, y_train, y_test = data
    # your code here
    d = {}
    y_hat_train = model.predict(x_train)
    y_hat_test = model.predict(x_test)
    d['name'] = name
    d['train_mse'] = mean_squared_error(y_train, y_hat_train)
    d['test_mse'] = mean_squared_error(y_test, y_hat_test)
    d['r2_train'] = r2_score(y_train, y_hat_train)
    d['r2_test'] = r2_score(y_test, y_hat_test)
    return d