# dashboard.py
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html, dcc
import pandas as pd
from components.callbacks import (
    region_dropdown,
    dept_dropdown,
    year_slider,
    material_dropdown,
    group_dropdown,
    sous_group_dropdown,
)

# Définition du layout (structure) de l'application
layout_DashBoard = html.Div(
    children=[
        html.H1("Dashboard Envirommental"),
        html.Div(region_dropdown),
        html.Div(dept_dropdown),
        html.Div(
            dcc.Graph(id="map_station", figure={}),
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(
            year_slider,
            style={"width": "35%", "margin-right": "auto", "margin-left": "12%"},
        ),
        # Corrected part: Wrap the dcc.Graph components in a list
        html.Div(
            [
                dcc.Graph(id="hist_annee", figure={}),
                dcc.Graph(id="hist_superficie", figure={}),
            ],
            style={
                "display": "flex",
                "justify-content": "center",
            },
        ),
        html.Div(material_dropdown),
        html.Div(dcc.Graph(id="cout_energetique", figure={})),
        html.Div(group_dropdown),
        html.Div(dcc.Graph(id="impact-climat-utilisation-sol", figure={})),
        html.Div(sous_group_dropdown),
        html.Div(dcc.Graph(id="impact-climat-ozone", figure={})),
    ],
    style={
        "text-align": "center",
        "font-size": 22,
        "background-image": 'url("/assets/7609662.jpg")',
        "background-size": "cover",  # Ajuste la taille de l'image pour couvrir l'élément div
        "width": "100%",  # Définir la largeur de l'élément div
        "height": "100%",
        "color": "black",
    },
)
