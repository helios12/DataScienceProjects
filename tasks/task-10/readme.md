# Task-10. Time Series - Forecast Ghana GDP
Link: [Task-10-MATH-ML-13.Time_series.ipynb](https://github.com/helios12/DataScienceProjects/blob/main/tasks/task-10/Task-10-MATH-ML-13.Time_series.ipynb)

The goal of the task is to analyze the time series of Ghana GDP from 1960 till 2021 and predict the GDP of Ghana using different forecasting models. For analysis I used seasonal decomposision, Dickey-Fuller test, auto-correlation and partial autocorrelation. For forecasting I used ARIMA and pmdarima for hyperpameter optimization. At the end I used a GARCH model to prdict the variance.

## Technology Stack
While working on this task I have mastered:

* python
* statsmodels.tsa
* matplotlib

## Conclusions
I have managed to forecast data with ARIMA and improved the forecast with interpolation of gaps and usage of pmdarima for the hyperparameters optimization. The GARCH model did not capture the patterns in the data possibly due to a low number of samples.

## Figures

Ghana GDP prediction with ARIMA using interpolation and hyperparameters optimization

![Ghana GDP prediction with ARIMA using interpolation and hyperparameters optimization](https://i.imgur.com/jl37Hmi.png)
