import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
import warnings
from pandas.api.types import is_numeric_dtype
from plotly.subplots import make_subplots
from scipy import stats


def display_histograms(data, cols=3, row_height=250):
    """For the purpose of the exploratory data analysis display all series of a dataframe 
    as subplot histograms with kde.

    Args:
        data (DataFrame): Dataframe for which series the histograms will be displayed.
        cols (int, optional): The subplots will be split into the provieded number of columns. Defaults to 3.
        row_height (int, optional): The height of the row of subplots. Defaults to 250.
    """
    rows, rows_rest = divmod(data.shape[1], cols)
    rows = rows + 1 if rows_rest else rows

    specs_cols = []
    for i in range(cols):
        specs_cols.append({"secondary_y": True})
    specs = []
    for i in range(rows):
        specs.append(specs_cols)

    fig = make_subplots(
        rows=rows, 
        cols=cols,
        subplot_titles=data.columns,
        specs=specs
    )

    i = 0
    for r in range(rows):
        for c in range(cols):
            if i == data.shape[1]:
                break
            
            fig.add_trace(
                go.Histogram(x=data.iloc[:, i], showlegend=False), 
                row=r + 1, 
                col=c + 1
            )
            
            if is_numeric_dtype(data[data.columns[i]]):
                kde = ff.create_distplot([data[data.columns[i]]], group_labels=[data.columns[i]])
                fig.add_trace(
                    go.Scatter(
                        kde['data'][1],
                        showlegend=False
                    ), 
                    row=r + 1, 
                    col=c + 1,
                    secondary_y=True
                )

            i += 1

    fig.update_layout(autosize=True, height=row_height*rows)

    fig.show('png')
    

def display_qqplot_histograms(data):
    """For the purpose of the exploratory data analysis display all series of a dataframe 
    as Q-Q plot and histograms with kde.

    Args:
        data (DataFrame): Dataframe for which series the Q-Q plots and histograms will be displayed.
    """
    warnings.simplefilter(action='ignore', category=FutureWarning)

    for i in range(data.shape[1]):
        plt.subplots(1, 2, figsize=(8, 3))

        if is_numeric_dtype(data[data.columns[i]]):
            plt.subplot(1, 2, 1)
            stats.probplot(data[data.columns[i]], plot=plt)

        plt.subplot(1, 2, 2)
        ax = sns.histplot(data=data, x=data.columns[i], kde=True, line_kws={'lw': 1, 'ls': '-'})
        ax.set_title(f'Hist {data.columns[i]}')
        ax.lines[0].set_color('crimson')

        plt.tight_layout()
        plt.show()
        

def display_pvalue_conclusion(p, alpha):
    """Display the conclusion based on the value of p-value and statistical significance.

    Args:
        p (float): p-value.
        alpha (float): Statistical significance.
    """
    if p <= alpha:
        print(
            f'''p-value={p:.3f} is less than or equal to the defined statistical significance α={alpha:.2f}. The null hypothesis can be rejected.'''
        )
    else:
        print(
            f'''p-value={p:.3f} is greater than the defined statistical significance α={alpha:.2f}. The null hypothesis cannot be rejected.'''
        )        

def display_shapiro(data, alpha):
    """Calculate the p-value based on the Shapiro-Wilk test and output the decision
    whether the provided data is normal or not.

    Args:
        data (Series): Data to be cheked for normality.
        alpha (float): Statistical significance.
    """
    _, p = stats.shapiro(data)

    if p <= alpha:
        print(
            f'''p-value={p:.3f} is less than or equal to the defined statistical significance α={alpha:.2f}. Data does not have normal distribution.'''
        )
    else:
        print(
            f'''p-value={p:.3f} is greater than the defined statistical significance α={alpha:.2f}. Data has normal distribution.'''
        )        
