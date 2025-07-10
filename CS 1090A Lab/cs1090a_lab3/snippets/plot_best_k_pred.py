# generate x values to predict on as before (for completeness)
x_lin = np.linspace(x.min(), x.max(), 1000)
x_lin = pd.DataFrame(x_lin, columns=['temp'])
x_lin.head()

# get predictions to plot
y_pred = best_knn.predict(x_lin)

# plot!
plt.plot(x_lin, y_pred)
plt.scatter(x_train, y_train, alpha=0.45, label='train')
plt.scatter(x_test, y_test, alpha=0.45, label='test')
plt.plot(x_lin, y_pred, c='k', label='predictions');
plt.xlabel('temp')
plt.ylabel('count')
plt.title(f'kNN Regression Model\n $k$={best_k}')
plt.legend();