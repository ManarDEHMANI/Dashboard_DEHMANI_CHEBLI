# Importations principales pour l'application Dash
from dash import html, dcc
from components.callbacks import (
    region_dropdown,
    dept_dropdown,
    year_slider,
    material_dropdown,
    group_dropdown,
    sous_group_dropdown,
)

# Définition de la structure (layout) de l'application pour le Dashboard
layout_DashBoard = html.Div(
    className="custom-row",
    children=[
        # Titre principal du tableau de bord, centré avec une couleur spécifique et une marge
        html.H1(
            "Dashboard Environnemental",
            style={"text-align": "center", "color": "black", "margin-bottom": "50px"},
        ),
        # Conteneur pour les sélecteurs de région et de département, avec style pour ajustement de largeur et marge automatique
        html.Div(
            [
                html.Div(region_dropdown),  # Sélecteur déroulant de région
                html.Div(dept_dropdown),  # Sélecteur déroulant de département
            ],
            style={
                "width": "100%",
                "margin": "auto",
            },
        ),
        # Carte affichant les stations de mesure, avec style pour centrer le contenu et hauteur fixée
        html.Div(
            dcc.Graph(id="map_station", figure={}),
            style={
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "height": "600px",
            },
        ),
        # Conteneur pour deux autres graphiques, chacun prenant la moitié de la largeur, avec défilement si nécessaire
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id="hist_annee", figure={}, responsive=True),
                        html.Div(
                            year_slider,
                            style={
                                "padding": "10px",
                            },
                        ),
                    ],
                    style={
                        "padding-bottom": "10px",
                        "width": "100%",
                        "height": "500px",
                        "overflow": "auto",
                    },
                ),
                html.Div(
                    [dcc.Graph(id="hist_superficie", figure={}, responsive=True)],
                    style={"width": "100%", "height": "500px", "overflow": "auto"},
                ),
            ],
            style={"display": "flex"},
        ),
        # Sélecteur de matériaux d'emballage et de groupe d'aliment
        html.Div(
            className="bg-grey",
            children=[material_dropdown, group_dropdown],
            style={"display": "flex"},
        ),
        html.Div(
            children=[
                # Histogramme pour le coût énergétique des matériaux
                html.Div(
                    [dcc.Graph(id="score_material", figure={})],
                    style={"width": "100%", "height": "500px", "overflow": "auto"},
                ),
                # Histogramme pour l'impact climatique sur l'utilisation du sol
                html.Div(
                    [dcc.Graph(id="utilisation-sol", figure={})],
                    style={"width": "100%", "height": "500px", "overflow": "auto"},
                ),
            ],
            style={"display": "flex"},
        ),
        # Sélecteur déroulant pour choisir des sous-groupes d'aliments
        html.Div(sous_group_dropdown),
        # Graphique pour l'impact climatique sur la couche d'ozone
        html.Div(dcc.Graph(id="impact-climat-ozone", figure={})),
    ],
    # Définir la couleur de fond pour toute la mise en page
    style={"backgroundColor": "#333333"},
)
