plt.scatter(x_test, resids)
plt.axhline(0, c='k')
plt.ylabel('standardized residuals')
plt.title('Linear Regression Residuals (Bike Share Data)')
plt.xlabel('$temp$');