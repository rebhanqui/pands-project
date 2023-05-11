import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading in the CSV file - acquired from:
# Read in CSV file
data = pd.read_csv("iris.csv")

print(data.head())
#prints off the top 5 rows of the data and then gives us the shape (number of rows and columns of the data file)
#Result:
#   sepal_length  sepal_width  petal_length  petal_width species
#0           5.1          3.5           1.4          0.2  setosa
#1           4.9          3.0           1.4          0.2  setosa
#2           4.7          3.2           1.3          0.2  setosa
#3           4.6          3.1           1.5          0.2  setosa
#4           5.0          3.6           1.4          0.2  setosa


print(data.shape)
#Result is 150 rows and 5 columns (does not include the row numbers column)
#(150, 5)

df = pd.DataFrame(data)
data.describe()


#Results:
#       sepal_length  sepal_width  petal_length  petal_width
#count    150.000000   150.000000    150.000000   150.000000
#mean       5.843333     3.054000      3.758667     1.198667
#std        0.828066     0.433594      1.764420     0.763161
#min        4.300000     2.000000      1.000000     0.100000
#25%        5.100000     2.800000      1.600000     0.300000
#50%        5.800000     3.000000      4.350000     1.300000
#75%        6.400000     3.300000      5.100000     1.800000
#max        7.900000     4.400000      6.900000     2.500000



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
######to stop duplicates come back to this!!!!######
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

#Saves a histogram of each variable to png files
x = 
y = ["setosa", "varsicolor", "virginica"]


plt.hist(x, y, ec="red")

plt.xlabel("Iris Species")
plt.ylabel("Iris Measurements")


plt.xticks(y)
plt.savefig("Test.png")
plt.close()
#histogram, 4, 5, 6 species compare sepal_length, width, petal_length, width

figure, ax = plt.subplots(2, 2, figsize=(8,8))
#https://www.statology.org/matplotlib-histogram-color/ - EC
ax[0,0].set_title("Sepal Length")
ax[0,0].hist(df['sepal_length'], color="#86f7ee", ec="#1ca398", bins=8)

ax[0,1].set_title("Sepal Width")
ax[0,1].hist(df['sepal_width'], color="#a996f2", ec="#371ca3", bins=8);

ax[1,0].set_title("Petal Length")
ax[1,0].hist(df['petal_length'], color="#74a684", ec="#125928", bins=8);

ax[1,1].set_title("Petal Width")
ax[1,1].hist(df['petal_width'], color="#faee46", ec="#736d1e", bins=8);

plt.savefig("Histograms")

#-----

plt.gcf().set_size_inches(14, 10)
sns.pairplot(df, hue="species")
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Overview of Species Comparison")

del df