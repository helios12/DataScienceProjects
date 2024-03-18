# Projects
In this folder I am giving a brief description of the projects, on which I have been working in the frames of the Data Science course at SkillFactory

## Folder Structure
### Project 1. Analysis of the HeadHunter.ru resumes
Link: [Project-1.HH_Resume_analysis.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/Project-1.HH_Resume_analysis.ipynb)

The goal of the project was to perform data preparation and clean-up before building a machine learning model. The model should be able to predict a candidate salary based on other candidate attributes. The preparation and the clean-up consisted of the following steps:

* Investigate data structure
* Transform data to make it more usable for data analyses. E.g., split columns containing multiple features into multiple columns
* Visual exploratory data analysis
* Data clean-up consisted of removing duplicates and removing outliers

#### Technology stack
While working on this project I have mastered:

* python
* pandas
* plotly express

#### Conclusions
* The raw CSV data has been transformed to a data structure with distinctly usable features
* Visual exploratory data analysis have shown that there is a dependency between the salary and other features like location, age, education, experience and unfortunately gender
* Around 200 duplicates and outliers have been removed as part of the data clean-up as well as all empty values have been handled

#### Screenshots
Link: [All screenshots](https://github.com/helios12/DataScienceProjects/tree/main/projects/img/project-1)

![Median salary heatmap by age and education](https://i.imgur.com/uxCl2ez.png) ![Relation between age and work experience](https://i.imgur.com/pfDjL0Y.png) ![Age distribution over log scale](https://i.imgur.com/IILwbR9.png)