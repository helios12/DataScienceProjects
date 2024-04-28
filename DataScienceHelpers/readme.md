# Data Science Helpers
In this folder I am collecting auxiliary functions for different standard data science tasks.
## Folder Structure
### Data Cleaning
#### Attributes Clean-up
Link: [DataCleaningAttributes.py](https://github.com/helios12/DataScienceProjects/blob/main/DataScienceHelpers/DataCleaningAttributes.py)

This file contains the code helping to identify those attributes, which could be ignored in the data analysis.

Functions:

* _find_attibutes_with_empty_ratio_ - within a pandas DataFrame find all attributes, which have more empty values than specified by a threshold.
* _find_low_information_attributes_ - within a pandas DataFrame find all attributes, which contain low information, e.g. too many identical values or too many distinct values.
#### Finding Outliers
Link: [DataCleaningOutliers.py](https://github.com/helios12/DataScienceProjects/blob/main/DataScienceHelpers/DataCleaningOutliers.py)

This file contains the code helping to identify outliers.

Functions:

* _find_outliers_iqr_ - for a column in a pandas DataFrame find outliers using the Interquartile range (IQR) method. By default it uses the default IQR of 1,5, but this can be adjusted to the left and to the right. Also a log scale can be applied to the column for lognormal distributions.
* _find_outliers_quantile_ - for a column in a pandas DataFrame find outliers using the quantiles defined on the left and on the right. This is the most inaccurate of the offered ourliers search methods.
* _find_outliers_z_score_ - for a column in a pandas DataFrame find outliers using the z-score method. By default it uses the default of 3 sigma, but this can be adjusted to the left and to the right. Also a log scale can be applied to the column for lognormal distributions.
* find_parameters_z_score - for a column in a pandas DataFrame find parameters mu, lower and upper bounds for the z-score method without finding the outliers. By default it uses the default of 3 sigma, but this can be adjusted to the left and to the right. Also a log scale can be applied to the column for lognormal distributions.

#### Exploratory Data Analysis
Link: [ExploratoryDataAnalysis.py](https://github.com/helios12/DataScienceProjects/blob/main/DataScienceHelpers/ExploratoryDataAnalysis.py)

This file contains the code helping in exploratory data analysis.

Functions:

* _display_histograms_ - for the purpose of the exploratory data analysis display all series of a dataframe as subplot histograms with kde.
* _display_qqplot_histograms_ - for the purpose of the exploratory data analysis display all series of a dataframe as Q-Q plot and histograms with kde.
* _display_pvalue_conclusion_ - display the conclusion based on the value of p-value and statistical significance.
* _display_shapiro_ - calculate the p-value based on the Shapiro-Wilk test and output the decision whether the provided data is normal or not.

#### Exploratory Data Analysis
Link: [Logging.py](https://github.com/helios12/DataScienceProjects/blob/main/DataScienceHelpers/Logging.py)

This file contains the code helping in logging the execution results.

Functions:

* _get_logger_ - creates a file to log into it and sets-up a logger.

## Technology Stack
While working on this library I have mastered:

* python
* numpy
* pandas
* plotly