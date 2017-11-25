# Frequency counts of a df var
df.var.value_counts(dropna = False)

# get complete info about df
df.info()

# get summary statistics numeric columns of a df
df.describe()

# visualize data for EDA
import matplotlib.pyplot as plt

#histogram
df.var.plot('hist')
plt.show()

#another way. inside plot give name of graph you want to see
# logx or logy is used to rescale the axis
# rot is used to rotate the name of the labels on axis by specified degrees
df['Existing Zoning Sqft'].plot(kind = 'hist', rot=70, logx=True, logy=True)

#boxplot:
df.boxplot(column = 'var1', by = 'var2')
plt.show()

#scatter plot: to visualize two numeric variables
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)

#read Tidy Data paper by Hadley wickham, phd

#melt dataframe to make it tidy: columns contain values and not variables
pd.melt(frame=df, id_vars=name, value_vars=['treatment a', 'treatment b'])
# id_vars => column you want to fix; value_vars => columns you want to melt

airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'],
value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp'], var_name = 'measurement',
value_name = 'reading')
# var_name => change the default name of variable to one of choice
# value_name => chnage the default name of value column to one of choice

#pivoting: opposite of melting
new_df = df.pivot(index = 'column_to_be_fixed',
columns = ['list of columns to be pivoted'],
values = 'column name from which values will be filled')
# if there are multiple observations for same index, pivot gives error. in such
# cases use pivot_table

new_df = df.pivot_table(index = 'list_of_columns_to_be_fixed',
columns = ['list of columns to be pivoted'],
values = 'column name from which values will be filled',
agg_func = np.mean)

#to get index column name of a dataframe
print (df.index)
#reset index of a dataframe with hierarchical index
df = df.reset_index()

#.str and split()
df['new_col'] = df.old_col.str[0]

#splitting a column
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'],
var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt['str_split'].str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())

#Concatenating data
#concat rows
concate_df = pd.concat([df1, df2], ignore_index=True)
#concat columns
concate_df = pd.concat([df1, df2], axis = 1)

# Finidng and Concatenating data. When there are a large number of files to
# be concatenated, manually writing each file name is not a good idea.
# glob function can help us find files with pattern matching
# * => any number of character; ? => single character
import glob
filename = glob.glob('*.csv') #finds all csv files in a folder
#now to concatenate, we need to provide filenames as list
list_data = []
for name in filename:
    data = pd.read_csv(name)
    list_data.append(data)
pd.concat(list_data) #concatenating huge number of df

#Merging data
pd.merge(left = df1, right = df2, on = None, # when common columns have different names
        left_on = 'common_column_name1', right_on = 'common_column_name2')
# it is not necessary to write 'on' when u r writing left_on, right_on

"""Claeaning Data for Analysis"""
#check data type of each column in dataframe
print (df.dtypes)

#convert a column to string
df['new_col'] = df['column_name'].astype(str)
#you can either create a new col to store new values or store in same old var

#convert a column to a category column representing categorical value such as male, female
df['new_col'] = df['column_name'].astype('category')
# it saves memory and is useful when df is used any other package

#convert to numeric
df['new_col'] = pd.to_numeric(df['column_name'], errors = coerce)
# errors = coerce replaces invalid values with NaN

#Using Regualar expressions to clean strings
import re
pattern = re.compile('^\$\d*\.\d{2}$')
# d=> digits; d* => more than 1 number of digits;
result = pattern.match('$17.89')

# drop duplicates in data
df = df.drop_duplicates()

# Missing data
df_new = df.dropna() #drop missing values from dataframe
gapminder = gapminder.dropna(axis=0, how='any')
df[[col1, col2]] = df[[col1, col2]].fillna(0)
df[[col1, col2]] = df[[col1, col2]].fillna('missing')
mean_value = df[col].mean()
df['col'] = df['col'].fillna(mean_value)

#assert
assert (df.col >= 0 ).all()
assert pd.notnull(gapminder.country).all()

#group by in pandas
data.groupby(['col1', 'col2'])['col3'].mean()
