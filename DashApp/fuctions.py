
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import  numpy as np
import plotly
plotly.tools.set_credentials_file(username='Johan.khanye', api_key='sy4KJxtUIOpZQxhAsHaw')
import plotly.plotly as py
# graph objects00
import plotly.graph_objs as go

# ///////////////////////////////////////////////////////////////////

# create markdown
def MarkdownText(text):
    return dcc.Markdown(text)

# Fuction to split column question to main question string
def get_col(col):
    dirt, semi_col = col.split('[')
    fin_col, dirt = semi_col.split(']')
    return fin_col

# Create bar-graph for our personality data.
def create_bar_graph(df, col):
    # Get key value pairs, key --> applicant responses and value --> counts of responses;
    keys = [k for k,v  in df[col].value_counts().items()];
    values = [v for k,v  in df[col].value_counts().items()];
    data = [go.Bar(x=keys,y=values,text=keys,textposition = 'auto')]
    # graph layout
    layout = go.Layout(
        title= get_col(col),
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
    return py.iplot(fig, filename='share_excitement-bar')

# Create scatter plot
def create_scatter_graph(df, x_col, y_col):
    return dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )