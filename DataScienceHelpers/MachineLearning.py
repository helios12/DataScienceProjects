import plotly.graph_objects as go
import numpy as np

from sklearn import metrics
from sklearn import model_selection


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
    

def plot_learning_curve(model, X, y, cv, scoring="f1", ax=None, title=""):
    """Plot a learning curve for a dataset unsing KFold cross validation.

    Args:
        model : Trained machine learning model.
        X (matrix): Observation matrix.
        y (vector): Target feature vector.
        cv : Cross validatorl
        scoring (str, optional): Scoring metric. Defaults to "f1".
        ax (array of axes, optional): Matplotlib array of axes. Defaults to None.
        title (str, optional): Diagram title. Defaults to "".
    """
    train_sizes, train_scores, valid_scores = model_selection.learning_curve(
        estimator=model, 
        X=X,  
        y=y,  
        cv=cv,
        scoring=scoring,
    )

    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(valid_scores, axis=1)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=train_scores_mean,
        mode='lines',
        name='train'
    ))
    fig.add_trace(go.Scatter(
        x=train_sizes,
        y=test_scores_mean,
        mode='lines',
        name='test'
    ))
    fig.update_layout(
        xaxis_title='Train data size',
        yaxis_title='Score',
        title=f'Learning curve: {title}',
        width=1000,
        height=500,
        yaxis_range=[0, 1]
    )
    fig.show('png')