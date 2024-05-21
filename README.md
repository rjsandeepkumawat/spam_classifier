# README: Iris Flower Classification

## Author: Sandeep Kumawat

## Batch: April 2024 (A48)

## Domain: Data Science

## Objective

The primary goal of this project is to develop a model capable of classifying iris flowers into distinct species based on their sepal and petal measurements.

## Libraries Utilized

The project employed several key libraries:

- numpy
- pandas
- sklearn.cluster.KMeans
- matplotlib.pyplot
- seaborn

## Dataset

The iris dataset, encompassing details about iris flowers such as sepal length, sepal width, petal length, petal width, and species, was loaded utilizing seaborn's `load_dataset` function.

## Data Exploration and Preprocessing

1. The dataset was loaded into a DataFrame using seaborn's `load_dataset` function, and the initial 5 rows were displayed via `df.head()`.
2. The 'species' column in the DataFrame was converted into numerical values using `pd.factorize(df['species'])`.
3. Descriptive statistics for the dataset were presented using `df.describe()`.
4. Missing values in the dataset were inspected using `df.isna().sum()`.

## Data Visualization

1. 3D scatter plots were generated to visualize the relationships among species, petal length, and petal width, as well as among species, sepal length, and sepal width, using `matplotlib.pyplot` and `mpl_toolkits.mplot3d.Axes3D`.
2. 2D scatter plots were crafted to depict the relationships between species and sepal length, as well as between species and sepal width, utilizing `seaborn.scatterplot`.

## Application of Elbow Technique for K-Means Clustering

1. The Elbow Technique was employed to ascertain the optimal number of clusters (K) based on the sum of squared errors (SSE).
2. The KMeans algorithm was initialized with varying values of K (ranging from 1 to 10), and SSE was computed for each K value.
3. A plot of K values against SSE was generated using `matplotlib.pyplot` to identify the "elbow point," indicative of the optimal number of clusters.

## Application of K-Means Algorithm

1. The KMeans algorithm was applied to the dataset with the optimal number of clusters (K=3) determined from the Elbow Technique.
2. Cluster labels were predicted for each data point in the dataset using `km.fit_predict(df[['petal_length','petal_width']])`.

## Accuracy Assessment

1. The confusion matrix was computed to assess the accuracy of the KMeans clustering.
2. The confusion matrix was visualized using `matplotlib.pyplot.imshow` and `plt.text` to display the true and predicted labels.
