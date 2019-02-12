# Functions to apply on visualisations notebook
# Import necessary libraries
import plotly
plotly.tools.set_credentials_file(username='Johan.khanye', api_key='sy4KJxtUIOpZQxhAsHaw')
import plotly.plotly as py
# graph objects00
import plotly.graph_objs as go


# Create histogram for our personality data.
def create_histogram(df, col, color='blue'):
    
    values = [v for k,v  in df[col].items()];
    data = [go.Histogram(x=values,
                   marker=dict(
        color=color,
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )))]
    # graph layout
    layout = go.Layout(
        title= col,
        yaxis=dict(
            title='Frequency of Applicants',
            titlefont=dict(
                size=20,
                color='rgb(107, 107, 107)'
            )
        )
    )

    # Show plot.
    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename=col)

