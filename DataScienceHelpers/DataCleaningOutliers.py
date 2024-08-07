import numpy as np


def find_outliers_iqr(data, feature, log_scale=False, lower_iqr=1.5, upper_iqr=1.5):
    """Using the IQR (Tukey) method calculate the outliers and cleaned data.

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
    x = apply_log_scale(data, feature, log_scale)
    
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - iqr*lower_iqr
    upper_bound = quartile_3 + iqr*upper_iqr
    outliers = data[(x<lower_bound) | (x>upper_bound)]
    cleaned = data[(x>=lower_bound) & (x<=upper_bound)]
    return outliers, cleaned


def find_parameters_iqr(data, feature, log_scale=False, lower_iqr=1.5, upper_iqr=1.5):
    """Calculate the paramethers for the IQR (Tukey) method, i.e. iqr, lower_bound, upper_bound.

    Args:
        data (DataFrame): DataFrame in which the outliers are being searched.
        feature (str): Attribute of the DataFrame to work on.
        log_scale (bool, optional): Defines whether to analyize in log scale. Defaults to False.
        lower_iqr (float, optional): IQR factor for lower boundary. Defaults to 1.5.
        upper_iqr (float, optional): IQR factor for upper boundary. Defaults to 1.5.

    Returns:
        iqr (float): Quartile 3 - Quartile 1.
        lower_bound (float): lower bound. Values below are outliers.
        upper_bound (float): upper bound. Values above are outliers.
    """
    x = apply_log_scale(data, feature, log_scale)
    
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - iqr*lower_iqr
    upper_bound = quartile_3 + iqr*upper_iqr
    return iqr, lower_bound, upper_bound


def find_outliers_z_score(data, feature, log_scale=False, left=3, right=3):
    """Using the z-score method calculate the outliers and cleaned data.

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
    x = apply_log_scale(data, feature, log_scale)
    
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left*sigma
    upper_bound = mu + right*sigma
    outliers = data[(x<lower_bound) | (x>upper_bound)]
    cleaned = data[(x>=lower_bound) & (x<=upper_bound)]
    return outliers, cleaned


def find_parameters_z_score(data, feature, log_scale=False, left=3, right=3):
    """Calculate the parameters for the z-score method, i.e. mu, lower_bound, upper_bound.

    Args:
        data (DataFrame): DataFrame for which the z-score method is being applied.
        feature (str): Attribute of the DataFrame to work on.
        log_scale (bool, optional): Defines whether to analyize in log scale. Defaults to False.
        left (float, optional): Standard deviation factor for the lower boundary. Defaults to 3.
        right (float, optional): Standard deviation factor for the upper boundary. Defaults to 3.

    Returns:
        mu (float): Mean value uf the provided feature.
        lower_bound (float): lower bound. Values below are outliers.
        upper_bound (float): upper bound. Values above are outliers.
    """
    x = apply_log_scale(data, feature, log_scale)
    
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left*sigma
    upper_bound = mu + right*sigma
    return mu, lower_bound, upper_bound


def find_outliers_quantile(data, feature, left=0.01, right=0.99):
    """Find the outliers and cleaned data by ignoring the data outside of the provided quantiles.

    Args:
        data (DataFrame): DataFrame in which the outliers are being searched.
        feature (str): Attribute of the DataFrame to work on.
        left (float, optional): Quantile to be skipped on the left side of the feature. Defaults to 0.01.
        right (float, optional): Quantile to be skipped on the right side of the feature. Defaults to 0.99.

    Returns:
        outliers (DataFrame): found outliers.
        cleaned (DataFrame): data cleaned from the outliers.
    """
    x = data[feature]
    lower_bound = x.quantile(left)
    upper_bound = x.quantile(right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned


def apply_log_scale(data, feature, log_scale):
    """Appliy log scale to a feature of the DataFrame.

    Args:
        data (DataFrame): DataFrame to which the log scale is being applied.
        feature (str): Attribute of the DataFrame to work on.
        log_scale (bool): Defines whether to apply the log scale.

    Returns:
        Series: Specific feature with applied log scale if necessary.
    """
    if log_scale:
        if data[data[feature] == 0][feature].count():
            x = np.log(data[feature] + 1)
        else:
            x = np.log(data[feature])
    else:
        x = data[feature]
    return x
