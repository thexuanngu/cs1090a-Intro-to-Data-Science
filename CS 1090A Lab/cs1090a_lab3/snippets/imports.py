# imports also appear again in the notebook below
# when these libraries first get used
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from warnings import simplefilter
simplefilter('ignore', category=(FutureWarning, UserWarning))