fig, axes = plt.subplots(nrows=len(all_preds)//2, ncols=2, figsize=(10,15))
axes = axes.ravel()
# We can zip as many iterables as we like together!
for k, cur_preds, ax in zip(ks, all_preds, axes):
    ax.scatter(x_train, y_train, alpha=0.45, label='train')
    ax.scatter(x_test, y_test, alpha=0.45, label='test')
    ax.plot(x_lin, cur_preds, c='k', label='predictions');
    ax.set_xlabel('temp')
    ax.set_ylabel('count')
    ax.set_title(f'kNN Regression Model (k={k})')
    ax.legend();
    
plt.tight_layout()