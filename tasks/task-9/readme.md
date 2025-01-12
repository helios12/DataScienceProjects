# Task-9. Text Classification Using Naive Bayes Classifier
Link: [Task-9.MATH-ML-7.Naive_bayes_classifier.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-9/Task-9.MATH-ML-7.Naive_bayes_classifier.ipynb)

The goal of the task is to use naive Bayes classifier to determine if an email is a spam or not. I used the ComplementNB classifier implementation from the sklearn library for that.

## Technology Stack
While working on this task I have mastered:

* python
* sklearn
* plotly express

## Conclusions
I have trained the ComplementNB classifier on the train dataset and applied it to the test dataset. The AUC (Area Under the ROC Curve) is 0.96 which indicates a good model performance. Then I have experimented with the alpha parameter of the classifier and got a slight increase in the F1-metric: 0.96 to 0.98.