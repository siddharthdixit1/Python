# Building a pandas dataframe from a set of lists
cities = ['Mumbai', 'Ghaziabad', 'Kolkata', 'Bangalore']
education = ['HSC', 'Engg', 'PG', 'Job']
time = ['18', '4', '1', '5']
# create a list of label to used as column names
list_labels = ['City', 'Purpose', 'No. of years']
# create a list of lists that will be used for values.
# This list is made from above given lists
list_values = [cities, education, time]
zipped_list = list(zip(list_labels, list_values)) #results in a list of tuples
data = dict(zipped_list)
df = pd.DataFrame(data)

#Broadcasting:
df[new_col]  = 'm' or df[new_col]  = 0
# this ensures that 0 or m is assigned to each row of new_col in df

#importing and exporting data in pandas
data = pd.read_csv(filepath, header=None or 0, names=col_names,
na_values={col_name : ['-1'], col2 : [pattern, pattern2]},
parse_dates = [[0,1,2]])

#header = None => the first line of data is not column names but data
#header = 0 is used in conjunction with names option to name cols during import stage
#names option enable us to provide column names to df while importing data
#na_values => special characters or values such as -1
# in data which represent missing values.
#you can ask pandas to replace these special characters with NaN
#parse_dates helps to create a date column from different columns which might be storing year, month, day in separate cols

#an example of data import
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
#header = 3 => top 3 lines of data are header
#comment = '#' => consider all lines starting with # as comment

#plotting with pandas: refer earlier notes
plt.savefig('plotname.png/jpg/pdf') #save plots

#An example
# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()


""" Visual Exploratory Data Analysis """
import matplotlib.pyplot as plt

df.plot(x= col name, y= [list of columns], kind = '')
# for kind option use hist for histogram, box for boxplot, line for line, scatter for scatter plots
# histogram has other options, range for range of bins, bins for number of bins
plt.tite('')
plt.xlabel('')
plt.ylabel('')
plt.show()
#drawing a histogram, pdf, cdf
df.col_name.plot(kind = 'hist', normed = True) #for pdf
df.col_name.plot(kind = 'hist', normed = True, cumulative=True) #for cdf

#An example
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)
# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0,.3))
plt.show()
# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', normed=True, bins=30, range=(0,.3), cumulative=True)
plt.show()


""" Quantitatively inspecting data """
#when u want to take mean column wise
df.mean(axis = 'columns')

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

#dataframe filtering based on a column
indices = iris['species'] == 'setosa'
setosa = iris.loc[indices,:]

#deleting a column
del df['col']
