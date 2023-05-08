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






#pair1 petal_length v petal_width
#pair2 sepal_length v sepal_width
#pair3 sepal_length v petal_length
#pair4 sepal_width v petal_width
#histogram3, 4, 5, 6 species compare sepal_length, width, petal_length, width