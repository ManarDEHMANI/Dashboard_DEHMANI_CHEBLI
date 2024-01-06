from dash import dcc, html

# Définition du style de la barre de navigation
navbar_style = {
    "background-color": "black",
    "padding": "30px",
    "text-align": "center",
}

nav_link_style = {
    "display": "inline-block",
    "margin-right": "10px",
    "text-decoration": "none",
    "color": "white",
    "text-align": "center",
}

# Style de l'icone
nav_img_style = {
    "margin-right": "10px",
}

# Création de la barre de navigation
navbar = html.Nav(
    style=navbar_style,
    children=[
        html.Img(src="/assets/logo.png", height="100px", style=nav_img_style),
        dcc.Link("Accueil", href="/accueil", style=nav_link_style),
        dcc.Link("Dashboard", href="/dashboard", style=nav_link_style),
    ],
)



