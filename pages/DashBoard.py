# Importations princiaples
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
        html.H1(
            "Dashboard Environnemental",
            style={
                "color": "#006400",  # Taille de police grande mais pas écrasante
                "fontWeight": "bold",  # Police en gras pour l'importance
                "textShadow": "0px 2px 2px lightgrey",  # Ombre portée légère pour le relief
                "textTransform": "uppercase",  # Texte en majuscules
                "textAlign": "center",  # Alignement du texte au centre
                "fontFamily": '"Open Sans", sans-serif',  # Police sans-serif moderne et lisible
            },
        ),  # Titre principal du tableau de bord
        html.Div(
            [
                html.Div(region_dropdown),  # Sélecteur de région
                html.Div(
                    dept_dropdown,
                ),  # Sélecteur de département
            ],
            style={
                "width": "50%",
                "margin": "auto",
            },
        ),
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
            dcc.Graph(id="score_material", figure={})
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
        "font-size": "22px",
        "width": "100%",
        "height": "100%",
        "color": "#333",  # Couleur du texte sombre pour un contraste élevé avec un fond clair
        "background": " #F5F5DC ",  # Couleur de fond légèrement grise pour un aspect doux et professionnel
        "background-repeat": "no-repeat",
        "background-attachment": "fixed",
    },
)
