import matplotlib.pyplot as plt
# Create a grid of axes
fig, axes = plt.subplots(nrows=len(cols)//2, ncols=2, figsize=(10,10))
# flatted the axes array to 1D
axes = axes.ravel()
# iterate over pairs of column names and axes
for c, ax in zip(cols, axes):
    # Use pandas' plot functionality
    df.plot(x=c, y='count', kind='scatter', ax=ax)
# add some padding between subplots
plt.tight_layout()