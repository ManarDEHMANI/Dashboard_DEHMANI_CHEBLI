import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html, dcc

# Crée un layout pour la page d'accueil
layout_acceuil = html.Div(
    # Définit le style de la division principale, qui couvrira l'écran entier (100vh pour 100% de la hauteur de la fenêtre)
    style={
        "background-image": 'url("/assets/bg.avif")',  # Image de fond tirée des ressources locales
        "background-size": "cover",  # L'image de fond couvre toute la division
        "width": "100%",  # Largeur de la division à 100% de la fenêtre
        "height": "100vh",  # Hauteur de la division à 100% de la hauteur de la fenêtre
        "color": "white",  # Couleur du texte à l'intérieur de la division
        "font-size": "24px",  # Taille de la police du texte
        "text-align": "center",  # Alignement du texte au centre
        "display": "flex",  # Utilise flexbox pour le positionnement
        "align-items": "center",  # Centre les éléments verticalement dans la division
    },
    children=[
        # Div interne qui contient un élément H1 pour le texte animé
        html.Div(
            html.H1(
                id="animated-text",
                style={
                    "text-align": "center",  # Alignement du texte au centre
                    "color": "white",  # Couleur du texte en blanc
                    "display": "flex",  # Utilise flexbox pour le positionnement
                    "align-items": "center",  # Centre les éléments verticalement
                    "justify-content": "center",  # Centre les éléments horizontalement
                    "margin-right": "50%",  # Marge à droite de 50% pour centrer le texte (cette méthode est inhabituelle pour centrer)
                    "margin-left": "50%",  # Marge à gauche de 50% pour centrer le texte (cette méthode est inhabituelle pour centrer)
                    "font-family": "cursive",  # Utilise une police cursive pour le texte
                },
            )
        ),
        # Composant Interval pour la mise à jour périodique, probablement utilisé pour animer le texte
        dcc.Interval(
            id="interval-component",
            interval=2000,  # Intervalle de mise à jour en millisecondes (2000ms = 2 seconde)
            n_intervals=0,  # Nombre initial d'intervalle passé (commence à 0)
        ),
    ],
)
