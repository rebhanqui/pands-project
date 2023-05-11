import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

#reading in the CSV file - acquired from:
# Read in CSV file
df = pd.read_csv("iris.csv")
print(df.head())
#Result:
#   sepal_length  sepal_width  petal_length  petal_width species
#0           5.1          3.5           1.4          0.2  setosa
#1           4.9          3.0           1.4          0.2  setosa
#2           4.7          3.2           1.3          0.2  setosa
#3           4.6          3.1           1.5          0.2  setosa
#4           5.0          3.6           1.4          0.2  setosa



print(df.shape)
#Result is 150 rows and 5 columns (does not include the row numbers column)
#(150, 5)

print(df.describe())
#                0           1           3           2
#count  150.000000  150.000000  150.000000  150.000000
#mean     5.843333    3.054000    3.758667    1.198667
#std      0.828066    0.433594    1.764420    0.763161
#min      4.300000    2.000000    1.000000    0.100000
#25%      5.100000    2.800000    1.600000    0.300000
#50%      5.800000    3.000000    4.350000    1.300000
#75%      6.400000    3.300000    5.100000    1.800000
#max      7.900000    4.400000    6.900000    2.500000
print(df.species.value_counts())



#using .info we can print the data types to avoid null data etc
print(df.info())
#Results:
#RangeIndex: 150 entries, 0 to 149
#Data columns (total 5 columns):
#    Column        Non-Null Count  Dtype  
#---  ------        --------------  -----  
#0   sepal_length  150 non-null    float64
#1   sepal_width   150 non-null    float64
#2   petal_length  150 non-null    float64
#3   petal_width   150 non-null    float64
#4   species       150 non-null    object 
#dtypes: float64(4), object(1)
#memory usage: 6.0+ KB


print(df.isnull().sum())
#Results:
#sepal_length    0
#sepal_width     0
#petal_length    0
#petal_width     0
#species         0
#dtype: int64

print(df.value_counts("species"))
#Results:
#species
#setosa        50
#versicolor    50
#virginica     50
#dtype: int64

#Outputs a summary of each variable to a single text file:


#------
#Outputs a scatter plot of each pair of variables:
#pair1 petal_length v petal_width
plt.gcf().set_size_inches(10, 8)
#sets the size of image in inches
sns.scatterplot(x="petal_width", y="petal_length", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Petal Width V Petal Length Scatterplot", dpi=200)
#saves the figure - saved with particular dpi(dots per inch = clarity of image) to fit all in image file
#https://stackoverflow.com/questions/13073045/matplotlib-savefig-size-control
plt.close()
#closes the file/image so duplicates do not form in charts and in legend
#https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another

#-----

#pair2 sepal_length v sepal_width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="sepal_width", y="sepal_length", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Sepal Width V Sepal Length Scatterplot", dpi=200)
plt.close()


#------

#pair3 sepal_length v petal_length
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_length", y="sepal_length", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Sepal Length V Petal Length Scatterplot", dpi=200)
plt.close()

#------

#pair4 sepal_width v petal_width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_width", y="sepal_width", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Sepal Width V Petal Width Scatterplot", dpi=200)
plt.close()

#------

#pair5 Sepal Length V Petal Width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_width", y="sepal_length", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Sepal Length V Petal Width Scatterplot", dpi=200)
plt.close()

#------

#pair6 Sepal Width V Petal Length
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.savefig("Sepal Width V Petal Length Scatterplot", dpi=200)
plt.close()

#------

#Saves a histogram of the 4 variables to png files
cols = ["sepal_length", "sepal_width", "petal_width", "petal_length"]
#renameing columns with dictionary to cols to save over dataframe
df.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
#like data.head shows every 50th row or the first row of each species data
df.loc[::50]

#https://www.statology.org/matplotlib-histogram-color/ - EC
#https://www.youtube.com/watch?v=02BFXhPQWHQ
#histogram, 4, 5, 6 species compare sepal_length, width, petal_length, width

# this histogram shows that the four attributes are either evenly distributed (bell shaped not binary)or not, sepal length and width are evenly distrib petal is not
fig, ax = plt.subplots(2, 2, figsize = (10, 8))
#saves 4 figures for each attribute into one figure
ax[0, 0].hist(df[0], label=cols[0], color="#F7EE77", ec="#DED66A")
ax[0, 1].hist(df[1], alpha=1, label=cols[1], color="#511FC2", ec="#1B0B42")
ax[1, 0].hist(df[2], alpha=0.6, label=cols[2], color="#F78E77", ec="#B86A58")
ax[1, 1].hist(df[3], alpha=0.5, label=cols[3], color="#41AB85", ec="#296B53")

#alpha 1 makes top most shape transparent fully, the rest lesser modes of transparancy

#needs legends on each!!!###############
plt.savefig("Histograms")


#-----

plt.gcf().set_size_inches(14, 10)
sns.pairplot(df, hue="species", palette="hls")
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Overview of Species Comparison")
