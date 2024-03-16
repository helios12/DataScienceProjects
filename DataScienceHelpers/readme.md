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
* _find_outliers_z_score_ - for a column in a pandas DataFrame find outliers using the z-score method. By default it uses the default of 3 sigma, but this can be adjusted to the left and to the right. Also a log scale can be applied to the column for lognormal distributions.
* _find_outliers_quantile_ - for a column in a pandas DataFrame find outliers using the quantiles defined on the left and on the right. This is the most inaccurate of the offered ourliers search methods.
## Technology Stack
While working on this library I have mastered:

* python
* numpy
* pandas