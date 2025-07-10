# visualizing the correlation between all variables
import seaborn as sns
sns.heatmap(df.corr(), cmap='coolwarm'),;