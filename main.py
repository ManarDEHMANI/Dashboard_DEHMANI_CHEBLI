# main.py
# Importation des modules nécessaires de Dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Importation des layouts des pages depuis les modules correspondants
from pages.DashBoard import layout_DashBoard
from pages.accueil import layout_acceuil
from pages.navbar import navbar

# Importation de l'instance de l'application Dash depuis le module app
from app import app

# Définition du layout (structure) de l'application
app.layout = html.Div(
    [
        dcc.Location(
            id="url", refresh=True
        ),  # Gère la barre d'adresse et l'URL de la page
        navbar,  # Affiche la barre de navigation
        html.Div(
            id="page-content"
        ),  # Contenu de la page qui sera mis à jour par callback
    ]
)


# Callback pour mettre à jour le contenu de la page en fonction de l'URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    # Si l'URL correspond à "/dashboard", affiche le layout du dashboard
    if pathname == "/dashboard":
        return layout_DashBoard
    else:
        # Sinon, affiche le layout de la page d'accueil
        return layout_acceuil


# Lancement de l'application en mode débogage
if __name__ == "__main__":
    app.run_server(debug=True)
