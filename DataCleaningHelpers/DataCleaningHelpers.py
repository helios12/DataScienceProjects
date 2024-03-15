import numpy as np


def attibutes_with_empty_ratio(data, threshold=0.3):
    """ Find attributes which have ratio of empty values higher than the provided threshold.

    Args:
        data (DataFrame): DataFrame in which the search for attributes is being performed.
        threshold (floar, optional): Threshold defining unaccabteble ratio of empty values. Defaults to 0.95.

    Returns:
        List: A list of tuples. Each element has the following structure: column name, 
        calculated empty values ratio.
    """
    cols_with_empty = []
    
    for col in data.columns:
        empty_ratio = data[col].isnull().sum() / data.shape[0]
        if empty_ratio > threshold:
            cols_with_empty.append((col, empty_ratio))
    
    return cols_with_empty


def outliers_iqr(data, feature, log_scale=False, lower_iqr=1.5, upper_iqr=1.5):
    """ Using the IQR (Tukey) method calculate the outliers and cleaned data.

    Args:
        data (DataFrame): DataFrame in which the outliers are being searched.
        feature (str): Attribute of the DataFrame to work on.
        log_scale (bool, optional): Defines whether to analyize in log scale. Defaults to False.
        lower_iqr (float, optional): IQR factor for lower boundary. Defaults to 1.5.
        upper_iqr (float, optional): IQR factor for upper boundary. Defaults to 1.5.

    Returns:
        outliers (DataFrame): found outliers.
        cleaned (DataFrame): data cleaned from the outliers.
    """
    if log_scale:
        if data[data[feature] == 0][feature].count():
            x = np.log(data[feature] + 1)
        else:
            x = np.log(data[feature])
    else:
        x = data[feature]
    
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - iqr*lower_iqr
    upper_bound = quartile_3 + iqr*upper_iqr
    outliers = data[(x<lower_bound) | (x>upper_bound)]
    cleaned = data[(x>=lower_bound) & (x<=upper_bound)]
    return outliers, cleaned


def outliers_z_score(data, feature, log_scale=False, left=3, right=3):
    """ Using the z-deviation method calculate the outliers and cleaned data.

    Args:
        data (DataFrame): DataFrame in which the outliers are being searched.
        feature (str): Attribute of the DataFrame to work on.
        log_scale (bool, optional): Defines whether to analyize in log scale. Defaults to False.
        left (float, optional): Standard deviation factor for the lower boundary. Defaults to 3.
        right (float, optional): Standard deviation factor for the upper boundary. Defaults to 3.

    Returns:
        outliers (DataFrame): found outliers.
        cleaned (DataFrame): data cleaned from the outliers.
    """
    if log_scale:
        if data[data[feature] == 0][feature].count():
            x = np.log(data[feature] + 1)
        else:
            x = np.log(data[feature])
    else:
        x = data[feature]
    
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left*sigma
    upper_bound = mu + right*sigma
    outliers = data[(x<lower_bound) | (x>upper_bound)]
    cleaned = data[(x>=lower_bound) & (x<=upper_bound)]
    return outliers, cleaned
    
    
def low_information_attributes(data, threshold=0.95):
    """ Find low information attributes, 
    i.e. having too many equal values or too many distinct values.

    Args:
        data (data): DataFrame in which the low information attributes are being searched.
        threshold (float, optional): Threshold defining low information attributes. Defaults to 0.95.

    Returns:
        List: A list of tuples. Each element has the following structure: column name, calculated value, 
        type of the calculated value (top_freq or nunique_ratio).
    """
    low_information_cols = []
    
    for col in data.columns:
        top_freq = data[col].value_counts(normalize=True).max()
        nunique_ratio = data[col].nunique() / data[col].count()
        if top_freq > threshold:
            low_information_cols.append((col, top_freq, 'top_freq'))
        if nunique_ratio > threshold:
            low_information_cols.append((col, nunique_ratio, 'nunique_ratio'))
    
    return low_information_cols