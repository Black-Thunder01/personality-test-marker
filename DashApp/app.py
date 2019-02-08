# -*- coding: utf-8 -*-
import dash
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from fuctions import MarkdownText,get_col

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# application data
data = pd.read_csv('../data/Copy of Applicant Personality Review (Dec 2018) (Responses) - Form Responses 1.csv')

app.layout = html.Div(children=[
    html.H1(children='Hello Umuzi Recruitment'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    # drop down to choose column to show it's bar graph
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    # This code prints the mark down
    MarkdownText('''### Total Results of applications by question'''),    

    dcc.Graph(
        id='First graph of our the Umuzi Application app',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)