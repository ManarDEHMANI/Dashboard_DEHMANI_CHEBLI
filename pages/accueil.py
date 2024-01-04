import dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash import html, dcc

layout_acceuil = html.Div(
    style={
        "background-image": 'url("/assets/7609662.jpg")',
        "background-size": "cover",  # Ajuste la taille de l'image pour couvrir l'élément div
        "width": "100%",  # Définir la largeur de l'élément div
        "height": "100vh",  # Définir la hauteur de l'élément div (100vh correspond à 100% de la hauteur de la fenêtre visible)
    },
)
