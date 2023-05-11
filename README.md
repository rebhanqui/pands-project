# pands-project

## Final Project for PANDS Module - HDIP in Data Analytics 2023

| Info | Details |
| -------- | -------- |
| Course: | KDATG_L08_Y1 |
| Author: | Rebecca Hannah Quinn |
| Student Number: | G00425671 |


### Investigating Fisher's Iris Data Set
The Iris Data Project is a well-known dataset in the machine learning community. It contains 150 samples of iris flowers, where each sample has four features/attributes: sepal length, sepal width, petal length, and petal width. The samples are equally distributed among three different species: setosa, versicolor, and virginica. This dataset is often used for classification tasks in machine learning and those learn data analytics.[^1]

For this project we are to creates various graphs from the data set downloaded so we can better understand the data within.

### Reading In The Data
To start we use some methods to read the data and make sense of what is there in order to be able to code the histogram and scatterplots that follow.

```python
df = pd.read_csv("iris.csv")
print(df.head())
print(df.shape())
```
Results of head() method[^2]:
|   |sepal_length | sepal_width | petal_length | petal_width | species |
|------|------------|-------------|------------|---------------|---------|
|0     |      5.1     |     3.5     |      1.4      |    0.2  |setosa|
|1     |     4.9      |    3.0      |     1.4       |   0.2  |setosa|
|2     |   4.7       |    3.2      |     1.3       |   0.2  |setosa|
|3     |   4.6       |   3.1      |     1.5      |    0.2  |setosa|
|4     |  5.0        |  3.6        |   1.4        |  0.2  |setosa|
|*this shows us the first 5 rows of data and their column titles which come in useful later to source data required*|

The results of the shape() method shows us that there are 5 columns and 150 rows of data in a simple result: (150, 5) (Rows, Columns)[^3]

Value_counts() used with "species" returns the count of each species in the date. In this case the result is even with 50 rows for each making up the 150 total:

|species|data values|
|----|-------|
|setosa    |    50|
|versicolor |   50|
|virginica   |  50|
|Name: species, dtype: int64|
|<class 'pandas.core.frame.DataFrame'>|

Finally, we check that there are no null values in the data and this results in:
|-------------|----|
|sepal_length |   0|
|sepal_width  |   0|
|petal_length |   0|
|petal_width  |   0|
|species      |   0|
|dtype: int64 |

### References
[^1]: https://gist.github.com/curran/a08a1080b88344b0c8a7
[^2]: https://www.w3schools.com/python/pandas/ref_df_head.asp#:~:text=Definition%20and%20Usage,a%20number%20is%20not%20specified.&text=Note%3A%20The%20column%20names%20will,addition%20to%20the%20specified%20rows.
[^3]: https://www.digitalocean.com/community/tutorials/python-shape-method#
