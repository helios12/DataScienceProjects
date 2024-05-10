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
* The features which were important for the built model are not fully matching with the features identified as significant by Chi2 and ANOVA.
* The lowest achieved MAPE metric was 0,13364. So, with the probability of around 86 % we can predict a hotel rating and in case of high deviations from the user's rating the Booking company can perform additional research on the hotel.
* The MAPE metric has been saved in Comet ML.
* Improvement of the MAPE could be achieved via the text analysis of the positive and negative reviews and by more thorough analisis of the tags.

## Figures
Aggregated hotel scores in different locations

![Aggregated hotel scores in different locations](https://i.imgur.com/9SztIjM.png)

Mean hotel scores for week number

![Mean hotel scores for week number](https://i.imgur.com/EYj87d2.png)

Most significant categorical variables for the target feature

![Most significant categorical variables for the target feature](https://i.imgur.com/QtOvzkA.png)

Most significant numerical variables for the target feature

![Most significant numerical variables for the target feature](https://i.imgur.com/LsmHiXN.png)

Correlation between the features using a heat map

![Correlation between the features using a heat map](https://i.imgur.com/JWIncp7.png)

Most important features of the regression model

![Most important features of the regression model](https://i.imgur.com/un7lg9O.png)