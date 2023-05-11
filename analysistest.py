import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
print(data.head())

cols = ["sepal_length", "sepal_width", "petal_width", "petal_length"]
#renameing columns with dictionary to cols to save over dataframe
data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
#like data.head shows every 50th row or the first row of each species data
data.loc[::50]

print(data.shape)
#shows how data is 
print(data.describe())
#                0           1           3           2
#count  150.000000  150.000000  150.000000  150.000000
#mean     5.843333    3.054000    3.758667    1.198667
#std      0.828066    0.433594    1.764420    0.763161
#min      4.300000    2.000000    1.000000    0.100000
#25%      5.100000    2.800000    1.600000    0.300000
#50%      5.800000    3.000000    4.350000    1.300000
#75%      6.400000    3.300000    5.100000    1.800000
#max      7.900000    4.400000    6.900000    2.500000
print(data.species.value_counts())

#plots 1 of 4 attributes
#plt.hist(data[0])



#changes the color of the scatter dots to signify each variant of iris
#dictionary for color assignment
colors = {"setosa":"violet", "virginica":"yellow", "varsicolor":"pink"}

plt.scatter(
    data[0],
    data[1],
    c=data["species"].map(colors))
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.title("Iris Data Scatterplot ")
plt.savefig("scatterplot.png")






