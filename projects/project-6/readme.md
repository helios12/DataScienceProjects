# Project 6. Customer segmentation
Link: [Project-6.Customer_segmentation.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-6/Project-6.Customer_segmentation.ipynb)

The goal is to segment ecommerce customers into clusters and to be able to predict to which claster new customers will belong. To do that we clean the data, perform basic exploratory data analysis, select the meaningful features and build the RFM (Recency/Frequency/Monetary) model. We experiment with feature space reduction using the PCA and t-SNE algorithms; use K-Means, EM-Model (GaussianMixture) and Agglomerative Clustering to build the segments. And finally we transition from the clustering to classification tasks to predict the cluster of new customers.





In the data preparation step I have used the following techniques:

* Connecting data from multiple data sources
* Plotly Express to visualize data
* One-hot encoder to encode categorical features
* Picked the most relevant features for the classification using filter based feature selection (SelectKBest)
* Normalized data using the MinMaxScaler

In the modelling step I went from simple to more complicated models as follows:

* Logistic regression
* Logistic regression with polynomial features
* Logistic regression with polynomial features and L2 regularization
* Decision tree
* Random forest
* Gradient boosting

## Technology stack
Whily working on this project I have mastered:

* python
* pandas
* Plotly Express
* scikit-learn

## Conclusions
* A good improvement in the metric value has been observed while moving from the basic logistic regression model to the gradient boosting.
* Regularization proved itself as a good mean against overfitting.

## Figures
Distribution of log trip duration by by vendor as a histogram

![Distribution of log trip duration by by vendor as a histogram](https://i.imgur.com/2ECZKak.png)

Relation between the pick-up day of week and pick-up hour

![Relation between the pick-up day of week and pick-up hour](https://i.imgur.com/cBpmXhX.png)

Geographic location of pick-up points

![Geographic location of pick-up points](https://i.imgur.com/fo8yzgG.png)

RMSE dynamics on train and validation datasets

![RMSE dynamics on train and validation datasets](https://i.imgur.com/IMCrCAR.png)
