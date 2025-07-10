plt.scatter(x_train, y_train, alpha=0.45, label='train')
plt.scatter(x_test, y_test, alpha=0.45, label='test')
plt.xlabel('temp')
plt.ylabel('count')
plt.title('Bike Share Data')
plt.legend();