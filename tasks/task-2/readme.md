# Task-2. Data science job analysis
Link: [Task-2.Data_Science_job_analysis.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-2/Task-2.Data_Science_job_analysis.ipynb)

The goal of the task was to perform data cleaning and exploratory data analysis (EDA) on a data set of data science related jobs. The EDA consisted of a visual analysis and of picking and performing statistical tests.

## Technology Stack
While working on this task I have mastered:

* python
* pandas
* plotly express
* scipy

## Conclusions
Answers have been given to the following posed questions:

* Is there a yearly salary growth for the "Data Scientist" jobs?
    * **_Answer:_** It has been statistically proven there is no ground to claim that there was a salary growth for "Data Scientist" jobs from 2020 to 2021, but there is salary growth from 2021 to 2022. This is matching the conclusion observed during the visual analysis (see figure 12).
* What is the relation between the salaries of the "Data Scientist" and "Data Engineer" jobs in 2022?
    * **_Answer:_** Based on the statistical test we cannot claim that data scientists salaries were higher than salaries of data engineers in the year 2022. This does not match the conclusion observed during the visual analysis (see figure 12).
* What is the relation between the "Data Scientist" salary and the company size?
    * **_Answer:_**  Statistical test proves that the medians of the salararies of data scientists in companies of different sizes are different. This confirms the observation which was made in the visual analysis (see figure 18). A more detailed analysis can be done to compare the salries pairwise between the companies of different sizes.
* Is there an interrelation between the company size and the presence of the "Data Scientist" or "Data Engineer" jobs in it?
    * **_Answer:_** The test has proven that there is a statistical interrelation between the company size and the presence of the "Data Scientist" and "Data Engineer" jobs in it. This ammends the conclusions which have been received during the visual analysis (see figure 18).

## Figures
Distribution of positions by salary in USD

![Distribution of positions by salary in USD](https://i.imgur.com/MUARH04.png)

Q-Q plot for remote and non-remote salaries in USD

![Q-Q plot for remote and non-remote salaries in USD](https://i.imgur.com/ABj79KZ.png)

Salary in USD distribution by employee residence

![Salary in USD distribution by employee residence](https://i.imgur.com/UVAUNtO.png)
