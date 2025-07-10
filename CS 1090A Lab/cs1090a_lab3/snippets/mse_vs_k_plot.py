# argmin gives the index of the lowest test MSE
best_idx = np.argmin(test_mses)
# which we cna use to select the k that corresponds to that minimum loss
best_k = ks[best_idx]

plt.plot(ks, train_mses, label='train')
plt.plot(ks, test_mses, label='test')
plt.axvline(best_k, c='k', ls='--', label=rf'best $k$={best_k}')
plt.xlabel(r'$k$')
plt.ylabel('MSE')
plt.title('kNN MSE loss as a function of $k$')
plt.legend();