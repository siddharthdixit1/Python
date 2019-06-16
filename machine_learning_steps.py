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
