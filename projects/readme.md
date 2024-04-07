# Projects
In this folder I am giving a brief description of the projects, on which I have been working in the frames of the Data Science course at SkillFactory

## Folder Structure
### Project 2. Analysis of the HeadHunter.ru job openings
Link: [Project-2.HH_Job_openings_analysis.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/Project-2.HH_Job_openings_analysis.ipynb)

The goal of the project was to practise SQL knowledge on a database which contained the HeadHunger job openings. Using the SQL queries different analyses should be made revealing the patterns in the data. The analysis consisted of th the following sections:

* Preliminary data analysis to investigate the data structure
* Detailed job openings analysis with the focus on the data in the 'vacancies' table
* Employer analysis to identify patterns in for employers and their job openings
* Data science job openings analysis to get more insights into this courese's industry 

#### Technology stack
Whily working on this project I have mastered:

* SQL
* python
* psycopg2
* pandas
* BeautifulSoup

#### Conclusions
* HeadHunter covers a large geographic area and includes jobs from many industries, which makes it attractive for a large number of employers and job seekers.
* The service has job openings from huge employers like Yandex as well as from very small companies. This proves that the business model of HeadHunter makes it very accessible for all types and sizes of businesses. 
* The fact that only 7% of the employers are involved into software development confirms that HeadHunter is not a purely IT oriented platform.
* With Yandex as the largest client represented in many geographic areas I would recommend HeadHunter to put a special team to handle Yandex to increase the customer satisfaction.
* Data related jobs and data science in particular are a solid part of all job openings base. However not too many positions are available for the beginners. 

#### Figures
HeadHunter database scheme
![HeadHunter database scheme](https://i.imgur.com/lxdiHWE.png)

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
![Median salary heatmap by age and education](https://i.imgur.com/uxCl2ez.png) ![Relation between age and work experience](https://i.imgur.com/pfDjL0Y.png) ![Age distribution over log scale](https://i.imgur.com/IILwbR9.png)