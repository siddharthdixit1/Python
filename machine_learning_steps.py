# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# if using Jupyter notebook then include following statement as well
%matplotlib inline

# load the dataset
data = pd.read_csv(filepath)

# explore data
data.info()

# summary statistics
data.describe()

# common data pre-processing steps
# missing data imputation
# encoding categorical variables
# standardizing the data

# after data preprocessing is complete split the data into train and test
from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X, y, random_state=111, test_size=0.3)
