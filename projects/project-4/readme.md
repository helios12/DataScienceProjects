# Project 4. Machine Learning - Classification
Link: [Project_4.ML.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-4/Project_4.ML.ipynb)

The goal of the project is to build a classification model which would predict if a customer is likely to open a deposit with the bank. That is achieved by going through the following steps of the CRISP DM process: requirements analysis, data analysis, data preparation, building a model, model evaluation. 

In the data preparation step I have used the following techniques:

* Label encoder and one-hot encoder to encode categorical features
* Picked the most relevant features for the classification using filter based feature selection (SelectKBest)
* Normalized data using the MinMaxScaler

In the modelling step I went from simple to more complicated models as follows:

* Logistic regression
* Decision tree
* Decision tree with hyper-parameter optimization using GridSearchCV
* Random forest
* Gradient boosting
* Stacking using decition tree and gradient boosting estimators and logistic regression final estimator
* Random forest with hyper-parameter optimization using optuna

## Technology stack
Whily working on this project I have mastered:

* python
* pandas
* scikit-learn
* optuna

## Conclusions
* With the provided data the improvement in the metric value between the basic and the complex model is not so high. 
* The best F1 classification metric has been achieved on random forest and gradient boosting 0.84 (0) and 0.82 (1).

## Figures
Age Distribution

![Age Distribution](https://i.imgur.com/zav8JEQ.png)

Call Duration Distribution

![Call Duration Distribution](https://i.imgur.com/IDf9xus.png)

Job Distribution

![Job Distribution](https://i.imgur.com/nXNn9E8.png)

Deposits Open by Marital Status and Education Level

![Deposits Open by Marital Status and Education Level](https://i.imgur.com/UfPJ6ty.png)
