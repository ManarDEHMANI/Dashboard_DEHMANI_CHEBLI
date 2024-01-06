import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html, dcc

layout_acceuil = html.Div(
style={
        "background-image": 'url("/assets/dash.jpg")',
        "background-size": "cover",  
        "width": "100%",  
        "height": "100vh", 
        "color": "white",  
        "font-size": "24px",
        "text-align": "center",
        "display": "flex",  
        "align-items": "center",
    },
    children=[
        html.Div(html.H1(id="animated-text",style={
           'text-align': 'center',
            'color': 'white',
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'center',
            'margin-right':'50%',
            'margin-left':'50%',
            'font-family': 'cursive', 

        })),
        dcc.Interval(
            id="interval-component",
            interval=1000, 
            n_intervals=0,
        ),
    ],
)
