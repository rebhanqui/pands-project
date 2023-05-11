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
```
|   |sepal_length | sepal_width | petal_length | petal_width | species |
|------|------------|-------------|------------|---------------|---------|
|0     |      5.1     |     3.5     |      1.4      |    0.2  |setosa|
|1     |     4.9      |    3.0      |     1.4       |   0.2  |setosa|
|2     |   4.7       |    3.2      |     1.3       |   0.2  |setosa|
|3     |   4.6       |   3.1      |     1.5      |    0.2  |setosa|
|4     |  5.0        |  3.6        |   1.4        |  0.2  |setosa|

### References
[^1]: https://gist.github.com/curran/a08a1080b88344b0c8a7
