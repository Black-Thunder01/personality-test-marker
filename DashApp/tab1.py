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
def generalTab1():
    return  html.Div([
                html.H3('Tab content 2'),
                dcc.Graph(
                    id='graph-2-tabs',
                    figure={
                        'data': [{
                            'x': [1, 2, 3],
                            'y': [5, 10, 6],
                            'type': 'bar'
                        }]
                    }
                )
            ])
