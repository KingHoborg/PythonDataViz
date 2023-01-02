# -*- coding: utf-8 -*-
"""
First Dash app

Created on Mon Jan  2 10:27:16 2023

@author: Sebastian Gumula
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {"background": '#123456',
          "text": '#7FDBFF'
          }

data = {"Fruit" : ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Quantity" : [4,1,2,2,4,5],
        "City" : ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        }

df = pd.DataFrame.from_dict(data)

fig = px.bar(df, x="Fruit", y="Quantity", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
    )

app.layout = html.Div(children=[
    html.H1(children= "Hello Dash"),
    html.Div(children= '''Your first amazing dash application. YAY.'''),
    
    dcc.Graph(
        id="example-graph",
        figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
    