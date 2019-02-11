# -*- coding: utf-8 -*-
import dash
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from fuctions import MarkdownText,get_col
# Import dependencies
from dash.dependencies import Input, Output
# import tabs
from tab1 import generalTab1

# ///////////////////////////////////////////////////////////////////
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# application data
# data = pd.read_csv('../data/Copy of Applicant Personality Review (Dec 2018) (Responses) - Form Responses 1.csv')

app.layout = html.Div(children=[
    html.H1(children='Umuzi Recruitment'),
    html.H2(children='Application visual statistics'),
    # Create the Session Tabs
    dcc.Tabs(id='UmuziStatsTab', value='mainTab', children=[
        dcc.Tab(label='General Tab', value="generalStatsTab"), # tab 1
        dcc.Tab(label='Sections', value='sectionsStatsTab'), #tab 2
        dcc.Tab(label='Opposing Descriptions', value='opposingDescriptionsStatsTab'),#tab 3
        dcc.Tab(label='Personal Truths', value='personalTruthsStatsTab'),#tab 4
    ]),
    html.Div(id='tabs-stats'),
    # This code prints the mark down
    MarkdownText('''## Total Results of applications by question'''),    
])
# Call back functions for the content of the Tabs

@app.callback(Output('tabs-stats', 'children'),
              [Input('UmuziStatsTab', 'value')])
def render_content(tab):
    if tab == 'generalStatsTab':
        # General tab
        return html.Div([
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
    elif tab == 'sectionsStatsTab':
        return None

if __name__ == '__main__':
    app.run_server(debug=True)