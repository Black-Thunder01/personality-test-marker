
# coding: utf-8

# In[1]:


# Functions to apply on visualisations notebook
# Import necessary libraries
import plotly
plotly.tools.set_credentials_file(username='Johan.khanye', api_key='sy4KJxtUIOpZQxhAsHaw')
import plotly.plotly as py
# graph objects00
import plotly.graph_objs as go


# In[2]:


# Fuction to split column question to main question string
def get_col(col):
    dirt, semi_col = col.split('[')
    fin_col, dirt = semi_col.split(']')
    return fin_col


# In[3]:


# Create bar-graph for our personality data.
def create_bar_graph(df, col, color='blue'):
    # Get key value pairs, key --> applicant responses and value --> counts of responses;
    keys = [k for k,v  in df[col].value_counts().items()];
    values = [v for k,v  in df[col].value_counts().items()];
    data = [go.Bar(x=keys,y=values,text=keys,textposition = 'auto',
                   marker=dict(
        color=color,
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )))]
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

