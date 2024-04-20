import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
            
            kde = ff.create_distplot([data[data.columns[i]]], group_labels=[data.columns[i]])

            fig.add_trace(
                go.Histogram(x=data.iloc[:, i], showlegend=False), 
                row=r + 1, 
                col=c + 1
            )
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

    fig.show()