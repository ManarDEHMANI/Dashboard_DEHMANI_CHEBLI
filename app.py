# app.py
import dash
import dash_bootstrap_components as dbc

# Thème Bootstrap pour l'application
bootstrap_theme = [
    dbc.themes.BOOTSTRAP,
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
]

# Création de l'application Dash
app = dash.Dash(__name__, external_stylesheets=bootstrap_theme)

server = app.server
app.config.suppress_callback_exceptions = True
