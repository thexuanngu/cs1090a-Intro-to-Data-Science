y_pred = lr.predict(x_lin)
plt.scatter(x_train, y_train, alpha=0.45, label='train')
plt.scatter(x_test, y_test, alpha=0.45, label='test')
plt.plot(x_lin, y_pred, c='k', label='predictions');
plt.xlabel('temp')
plt.ylabel('count')
plt.title('Linear Regression Model')
plt.legend();