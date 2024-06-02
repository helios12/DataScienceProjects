# Task-4. Supervised Learning: Classification
Link: [Task-4.Classification_Of_Bank_Customers_Churn.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-4/Task-4.Classification_Of_Bank_Customers_Churn.ipynb)

The goal of the task was to explore the following models of classification: logistic regression, decision tree and random forest on the bank customer churn dataset and perform some basic set-up of the models, like respectively regularization type, C-coefficient, max depth, max leaf objects, and identify optimum probability thresholds. Preceding the modeling some basic data cleaning and exploratory data analysis must be performed.

## Technology Stack
While working on this task I have mastered:

* python
* sklearn
* pandas
* plotly express

## Conclusions
F1 metric has been identified as the most fitting for this task. The best results of the metric after optimizing the probability threshold has been shown on the logistic regression model using normalized data and polynomial features.

## Figures
F1 values based on variable C coefficient with regularization 'l1'

![F1 values based on variable C coefficient with regularization 'l1'](https://i.imgur.com/HbV9bdM.png)

Relation between the F1 metric and the probability threshold

![Relation between the F1 metric and the probability threshold](https://i.imgur.com/vsdEMWq.png)