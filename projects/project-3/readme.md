# Project 3. Hotel reviews analysis
Link: [Project-3.Hotel_reviews_analysis.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/projects/project-3/Project-3.Hotel_reviews_analysis.ipynb)

The goal of the project was to perform data cleaning, exploratory data analysis, build a regression model and evaluate the quality of the model prediciton results. Working on the project included the following activities:

* Data cleaning: removing duplicates, removing outliers and removing low-information attributes
* Exploratory data analysis: feature engineering, encoding categorical features, normalization and standardization, estimate of feature significance and multicollinearity
* Building a regression model using the scikit-learn RandomForestRegressor
* Calculating the MAPE (mean absolute percentage error) using scikit-learn metrics
* Logged the results to Comet ML

## Technology stack
Whily working on this project I have mastered:

* python
* pandas
* scikit-learn
* geopy

## Conclusions
* Not all activities performed as part of the exploratory data analysis improved the MAPE metric value. E.g., normalization, standardization and removing the multicollinear features did not improve MAPE.
* While working with dates, better results have been achieved by parsing the date into multiple parts (e.g., year, month, day and day of week) and then encoding the fields as categories.
* The lowest achieved MAPE metric was 0,13364. So, with the probability of around 86 % we can predict a hotel rating and in case of high deviations from the user's rating the Booking company can perform additional research on the hotel. 

## Figures
Most significant categorical variables for the target feature

![Most significant categorical variables for the target feature](https://i.imgur.com/ifgQE92.png)

Most significant numerical variables for the target feature

![Most significant numerical variables for the target feature](https://i.imgur.com/TwFf7Kp.png)

Correlation between the numeric features using a heat map

![Correlation between the numeric features using a heat map](https://i.imgur.com/dEE4LaJ.png)