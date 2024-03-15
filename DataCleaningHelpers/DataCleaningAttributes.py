def find_attibutes_with_empty_ratio(data, threshold=0.3):
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


def find_low_information_attributes(data, threshold=0.95):
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