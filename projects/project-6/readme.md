# Project 6. Customer Segmentation
Link: [Project-6.Customer_segmentation.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-6/Project-6.Customer_segmentation.ipynb)

The goal is to segment ecommerce customers into clusters and to be able to predict to which claster new customers will belong. To do that we clean the data, perform basic exploratory data analysis, select the meaningful features and build the RFM (Recency/Frequency/Monetary) model. We experiment with feature space reduction using the PCA and t-SNE algorithms; use K-Means, EM-Model (GaussianMixture) and Agglomerative Clustering to build the segments. And finally we transition from the clustering to classification tasks to predict the cluster of new customers.

In the data preparation step I have used the following techniques:

* Grouping data in multiple different ways
* Plotly Express to visualize data
* Pipelines to streamline modelling
* MinMax and Standard scalers to normalize data
* PCA and t-SNE algorythims for dimensionality reduction
* K-Means, EM-Model and Agglomerative Clustering models
* GridSearchCV for hyper parameters optimization

## Technology stack
Whily working on this project I have mastered:

* python
* pandas
* Plotly Express
* scikit-learn

## Conclusions
* Customers have been distributed over 7 clusters, where each cluster has a specific business meaning
* Radar chart is a powerful tool to present different parameters of clusters
* Classification can be used to determine to which cluster new data belongs

## Figures
Recency/Frequency/Monetary distribution without outliers

![Recency/Frequency/Monetary distribution without outliers](https://i.imgur.com/ud9PzpR.png)

Clustered two-dimensional RFM distribution

![Clustered two-dimensional RFM distribution](https://i.imgur.com/ytbLqCX.png)

Two-dimensional RFM distribution by t-SNE decomposition

![Two-dimensional RFM distribution by t-SNE decomposition](https://i.imgur.com/gxt2IZy.png)

Cluster distribution: radar chart

![Cluster distribution: radar chart](https://i.imgur.com/9lvNJpi.png)
