from dash import html, dcc
from components.callbacks import (
    region_dropdown,
    dept_dropdown,
    year_slider,
    material_dropdown,
    group_dropdown,
    sous_group_dropdown,
)

# Définition du layout (structure) de l'application pour le Dashboard
layout_DashBoard = html.Div(
    children=[
        html.H1("Dashboard Environnemental"),  # Titre principal du tableau de bord
        html.Div(region_dropdown),  # Sélecteur de région
        html.Div(dept_dropdown),  # Sélecteur de département
        html.Div(
            dcc.Graph(id="map_station", figure={}),
            style={"display": "flex", "justify-content": "center"},
        ),  # Carte des stations météorologiques
        html.Div(
            year_slider,
            style={"width": "35%", "margin-right": "auto", "margin-left": "12%"},
        ),  # Sélecteur d'année avec slider
        html.Div(
            [
                dcc.Graph(id="hist_annee", figure={}),  # Histogramme par année
                dcc.Graph(id="hist_superficie", figure={}),  # Histogramme de superficie
            ],
            style={
                "display": "flex",
                "justify-content": "center",
            },
        ),
        html.Div(material_dropdown),  # Sélecteur de matériau d'emballage
        html.Div(
            dcc.Graph(id="cout_energetique", figure={})
        ),  # Histogramme de coût énergétique
        html.Div(group_dropdown),  # Sélecteur de groupe d'aliments
        html.Div(
            dcc.Graph(id="impact-climat-utilisation-sol", figure={})
        ),  # Histogramme d'impact climatique sur l'utilisation du sol
        html.Div(sous_group_dropdown),  # Sélecteur de sous-groupe d'aliments
        html.Div(
            dcc.Graph(id="impact-climat-ozone", figure={})
        ),  # Histogramme d'impact climatique sur la couche d'ozone
    ],
    style={
        "text-align": "center",
        "font-size": 22,
        "background-image": 'url("/assets/7609662.jpg")',  # Image de fond
        "background-size": "cover",  # Ajuste la taille de l'image pour couvrir l'élément div
        "width": "100%",  # Définir la largeur de l'élément div
        "height": "100%",  # Définir la hauteur de l'élément div
        "color": "black",  # Couleur du texte
    },
)
