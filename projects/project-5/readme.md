# Project 5. Taxi Ride Duration
Link: [Project-5.Taxi_ride_duration.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-5/Project-5.Taxi_ride_duration.ipynb)

The goal of the project is to build a regression model to predict a taxi ride duration and thus be able to calculate the taxi ride price. Before that the data gets cleaned, basic exploratory data analysis are performed, categorical features get encoded, important features get selected and and the data is normalied. Then several regression models are being built and compared with each other using the Root Mean Squared Log Error metric.

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
