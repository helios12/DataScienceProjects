from sklearn import metrics

def display_metrics(y, y_pred):
    """Display the following metrics for the true and predicted y: R2, MAE, MAPE and MSE.

    Args:
        y (Series): True y value.
        y_pred (Series): Predicted y value.
    """
    print(f'R2: {metrics.r2_score(y, y_pred):.3f}')
    print(f'MAE: {metrics.mean_absolute_error(y, y_pred):.0f}')
    print(f'MAPE: {metrics.mean_absolute_percentage_error(y, y_pred) * 100:.0f}')
    print(f'MSE: {metrics.mean_squared_error(y, y_pred):.0f}')