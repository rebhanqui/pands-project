import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading in the CSV file - acquired from:
df = pd.read_csv("iris.csv")

#prints off the top 5 rows of the data and then gives us the shape (number of rows and columns of the data file)
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

#using .info we can print the data types to avoid null data etc
print(df.info())
#Results:
#<class 'pandas.core.frame.DataFrame'>
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
print("The information gathered from the dataset shows us that the is only 1 catagorical column and all others are numeric type with non-Null entries")

print("\nNext we will use the descibe() method to get a good picture of the distribution of data\n")
print(df.describe())
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

print("\nTo check for any missing values we use isnull() method with sum to get the total, for this dataset there are no missing value.")
print(df.isnull().sum())
#Results:
#sepal_length    0
#sepal_width     0
#petal_length    0
#petal_width     0
#species         0
#dtype: int64

print(".value_counts shows whether the dataset is balanced or not - equal amounts of rows per species and the data type of each value")
print(df.value_counts("species"))
#Results:
#species
#setosa        50
#versicolor    50
#virginica     50
#dtype: int64


plt.gcf().set_size_inches(14, 10)
#pair1 petal_length v petal_width
sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
# Placing Legend outside the Figure
#saves the figure - saved with particular dpi(dots per inch = clarity of image) to fit all in image file
#https://stackoverflow.com/questions/13073045/matplotlib-savefig-size-control

#sets the size of image in inches
plt.show()
#plt.savefig("Petal Width V Petal Length Scatterplot", dpi=200)


df2 = pd.read_csv("iris.csv")
#pair2 sepal_length v sepal_width

sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=df2)
# Placing Legend outside the Figure

#shows the figure
#plt.show()
#saves the figure - saved with particular dpi(dots per inch = clarity of image) to fit all in image file
#https://stackoverflow.com/questions/13073045/matplotlib-savefig-size-control

#sets the size of image in inches
plt.show()
#plt.savefig("Sepal Width V Sepal Length Scatterplot", dpi=200)

plt.legend(bbox_to_anchor=(1, 1), loc=2)
print("Species Setosa has smaller sepal lengths but larger sepal widths.\nVersicolor Species lies in the middle of the other two species in terms of sepal length and width.\nSpecies Virginica has larger sepal lengths but smaller sepal widths.")


#pair3 sepal_length v petal_length
#pair4 sepal_width v petal_width
#histogram3, 4, 5, 6 species compare sepal_length, width, petal_length, width

axis = df.plot.hist(bins=30, alpha=0.5)
axis.set_xlabel('Size in cm')
plt.show()

sns.pairplot(df, hue='species')
plt.show()