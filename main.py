# main.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pages.DashBoard import layout_DashBoard
from pages.accueil import layout_acceuil
from pages.navbar import navbar
from app import app

# Call the create_dashboard_layout function and pass the app instance
# Définition du layout (structure) de l'application
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=True),
        navbar,
        html.Div(id="page-content"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dashboard":
        return layout_DashBoard
    else:
        return layout_acceuil


# Lancement de l'application
if __name__ == "__main__":
    app.run_server(debug=True)
