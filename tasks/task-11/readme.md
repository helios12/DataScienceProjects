# Task-11. A/B Testing - Analysis of the Effectiveness of Two Landing Page Variants
Link: [Task-11-AB-Testing-Two-Landing-Pages.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-11/Task-11-AB-Testing-Two-Landing-Pages.ipynb)

The goal of this task is to analyze data which has been collected as part of an A/B test. By using statistic tests and confidence intervals we need to identify whether conversion rate and average bill are better in one of the groups (A or B). For conversion rate I have used the proportions Z-test and for the average bill I have used the T-test. For both metrics I have calculated the confidence intervals and for the conversion rate I have calculated a confidence interval of conversion rates differences. 

## Technology Stack
While working on this task I have mastered:

* python
* scipy.stats
* statsmodels.stats

## Conclusions
Based on the statistic tests and analysis of confidence intervals I can state that:
* The conversion rates in both groups are statistically the same.
* The average bill in the the group B is larger than in the group A. Although it must be noted that the cumulative average bill has not stabilized and it would make sense to prolong the test for more accurate results.
