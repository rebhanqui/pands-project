import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading in the CSV file - acquired from:
# Read in CSV file
#prints the top 5 rows of the data
df = pd.read_csv("iris.csv")
print(df.head())

#checks how many rows and columns
print(df.shape)
#Result is 150 rows and 5 columns (does not include the row numbers column)

#checks the count of each species
print(df.value_counts("species"))

#checks for null values
print(df.isnull().sum())

#summarise the information in order to read/write new file
summarize = df.describe()
#Outputs a summary of each variable to a single text file:
with open ("summary.txt", "w+") as file:
    file.write(summarize.to_string())
file.close()

#------
#Outputs a scatter plot of each pair of variables:
#pair1 petal_length v petal_width
plt.gcf().set_size_inches(10, 8)
#sets the size of image in inches
sns.scatterplot(x="petal_width", y="petal_length", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
#palette creates colors for scatter dots https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("pwvplscatterplot.png", dpi=200)
#saves the figure - saved with particular dpi(dots per inch = clarity of image) to fit all in image file
#https://stackoverflow.com/questions/13073045/matplotlib-savefig-size-control
plt.close()
#closes the file/image so duplicates do not form in charts and in legend
#https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another

#-----

#pair2 sepal_length v sepal_width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="sepal_width", y="sepal_length", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("swvslscatterplot.png", dpi=200)
plt.close()


#------

#pair3 sepal_length v petal_length
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_length", y="sepal_length", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("slvplscatterplot.png", dpi=200)
plt.close()

#------

#pair4 sepal_width v petal_width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_width", y="sepal_width", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("swvpwcatterplot.png", dpi=200)
plt.close()

#------

#pair5 Sepal Length V Petal Width
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="petal_width", y="sepal_length", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("slvpwscatterplot.png", dpi=200)
plt.close()

#------

#pair6 Sepal Width V Petal Length
plt.gcf().set_size_inches(10, 8)
sns.scatterplot(x="sepal_width", y="petal_length", hue="species", data=df, palette=["#A74DAD", "#71DDFF", "#396B2D"])
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("swvplscatterplot.png", dpi=200)
plt.close()

#------

#Saves a histogram of the 4 variables to png files
cols = ["sepal_length", "sepal_width", "petal_width", "petal_length"]
#renameing columns with dictionary to cols to save over dataframe
df.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
#like data.head shows every 50th row or the first row of each species data
df.loc[::50]

#histogram, 4, 5, 6 species compare sepal_length, width, petal_length, width
# this histogram shows that the four attributes are either evenly distributed (bell shaped not binary)or not, sepal length and width are evenly distrib petal is not
fig, ax = plt.subplots(2, 2, figsize = (15, 10))
#saves 4 figures for each attribute into one figure

ax[0, 0].set_title("Sepal Length")
ax[0, 0].hist(df[0], label=cols[0], color="#F7EE77", ec="#DED66A")
ax[0, 1].set_title("Sepal Width")
ax[0, 1].hist(df[1], alpha=1, label=cols[1], color="#511FC2", ec="#1B0B42")
ax[1, 0].set_title("Petal Width")
ax[1, 0].hist(df[2], alpha=0.6, label=cols[2], color="#F78E77", ec="#B86A58")
ax[1, 1].set_title("Petal Width")
ax[1, 1].hist(df[3], alpha=0.5, label=cols[3], color="#41AB85", ec="#296B53")
#alpha 1 makes top most shape transparent fully, the rest lesser modes of transparancy

plt.savefig("Histograms.png")


#-----

plt.gcf().set_size_inches(14, 10)
sns.pairplot(df, hue="species", palette="hls")
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.savefig("Overview of Species Comparison")
