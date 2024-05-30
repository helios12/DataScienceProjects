from sklearn import metrics


def display_classification_metrics(y, y_pred):
    """Display the following classification task metrics: Accuracy, Precision, Recall, F1.

    Args:
        y (Series): True y value.
        y_pred (Series): Predicted y value.
    """
    print(f'Accuracy: {metrics.accuracy_score(y, y_pred):.2f}')
    print(f'Precision: {metrics.precision_score(y, y_pred):.2f}')
    print(f'Recall: {metrics.recall_score(y, y_pred):.2f}')
    print(f'F1: {metrics.f1_score(y, y_pred):.2f}')
    
    
def display_regression_metrics(y, y_pred):
    """Display the following regression metrics: R2, MAE, MAPE and MSE.

    Args:
        y (Series): True y value.
        y_pred (Series): Predicted y value.
    """
    print(f'R2: {metrics.r2_score(y, y_pred):.3f}')
    print(f'MAE: {metrics.mean_absolute_error(y, y_pred):.0f}')
    print(f'MAPE: {metrics.mean_absolute_percentage_error(y, y_pred) * 100:.0f}')
    print(f'MSE: {metrics.mean_squared_error(y, y_pred):.0f}')