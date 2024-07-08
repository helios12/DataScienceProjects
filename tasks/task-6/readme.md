# Task-6. Machine Learning. Hyper Parameters Optimization
Link: [Task-6.ML_predicting_biological_response.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-6/Task-6.ML_predicting_biological_response.ipynb)

The goal of the task was to apply different hyper parameter optimization methods like Grid Search, Random Search and Tree-Structured Parzen Estimators for two types of models Logistic Regression and Random Forest. F1-score metric must be calculated on all applied methods and thus the methods can be compared between each other on a given set of data.

## Technology Stack
While working on this task I have mastered:

* python
* sklearn
* hyperopt
* optuna

## Conclusions
In case of usage of hyper parameter optimization F1-score metric on the test data has always been better than on the basic model without optimizaiton. Random Forest showed better results than the Logistic Regression although it tends to overfitting.