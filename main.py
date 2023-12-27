# Importation des modules nécessaires
import dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash import html, dcc

# Chargement des données depuis un fichier CSV
df = pd.read_csv("data/stations_data.csv", encoding="latin1")
df["annee_mise_en_service"] = pd.to_datetime(df["Annee"]).dt.year

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Définition des options pour les dropdowns (menus déroulants)
region_options = [{"label": "Toutes les Régions", "value": "Toutes"}] + [
    {"label": r, "value": r} for r in df["Region"].unique()
]
dept_options = [{"label": "Tous les Départements", "value": "Tous"}] + [
    {"label": d, "value": d} for d in df["Departement"].unique()
]

# Création des dropdowns pour sélectionner une région et un département
region_dropdown = dcc.Dropdown(
    id="region-dropdown",
    options=region_options,
    value="Toutes",
    clearable=False,
    style={"width": "50%", "margin": "auto"},
)

dept_dropdown = dcc.Dropdown(
    id="dept-dropdown",
    options=dept_options,
    value="Tous",
    clearable=False,
    style={"width": "50%", "margin": "auto"},
)

# Calculer les années avec un pas de 20
years_with_step = list(
    range(df["annee_mise_en_service"].min(), df["annee_mise_en_service"].max() + 1, 20)
)

# Ajouter manuellement la marque pour l'année maximale
years_with_step.append(df["annee_mise_en_service"].max())

# Créer le RangeSlider avec les marques
year_slider = dcc.RangeSlider(
    id="range-slider-year",
    min=df["annee_mise_en_service"].min(),
    max=df["annee_mise_en_service"].max(),
    step=1,
    marks={str(year): str(year) for year in years_with_step},
    value=[df["annee_mise_en_service"].min(), df["annee_mise_en_service"].max()],
)

# Définition du layout (structure) de l'application
app.layout = html.Div(
    children=[
        html.H1(
            "Dashborat Envirommental",
        ),
        html.Div(region_dropdown),
        html.Div(dept_dropdown),
        html.Div(
            dcc.Graph(id="map_station", figure={}),
            style={"display": "flex", "justify-content": "center"},
        ),
        html.Div(year_slider, style={"width": "50%", "margin": "auto"}),
        html.Div(
            dcc.Graph(id="hist_annee", figure={}),
            style={"display": "flex", "justify-content": "center"},
        ),
    ],
    style={
        "text-align": "center",
        "font-size": 22,
        "background-color": "white",
        "color": "black",
    },  # Définir le fond en noir et la couleur du texte en blanc
)


# Callback pour mettre à jour la carte et synchroniser les sélections
@app.callback(
    [
        Output(component_id="map_station", component_property="figure"),
        Output(component_id="region-dropdown", component_property="value"),
        Output(component_id="dept-dropdown", component_property="value"),
    ],
    [
        Input(component_id="region-dropdown", component_property="value"),
        Input(component_id="dept-dropdown", component_property="value"),
    ],
)
def update_map_and_selectors(selected_region, selected_dept):
    trigger = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    if trigger == "dept-dropdown" and selected_dept != "Tous":
        filtered_df = df[df["Departement"] == selected_dept]
        selected_region = (
            filtered_df["Region"].iloc[0] if not filtered_df.empty else "Toutes"
        )

    elif trigger == "region-dropdown":
        if selected_region != "Toutes":
            filtered_df = df[df["Region"] == selected_region]
            if not df[df["Departement"] == selected_dept]["Region"].equals(
                filtered_df["Region"]
            ):
                selected_dept = "Tous"
        else:
            filtered_df = df
            selected_dept = "Tous"
    else:
        filtered_df = df

    fig = px.scatter_mapbox(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        color="Region",
        hover_data=["Station", "Departement", "Region"],
    )
    fig.update_layout(
        mapbox=dict(
            center=dict(lat=46.6031, lon=1.8883),
            style="open-street-map",
            zoom=5,
        ),
        title=dict(
            text="Stations de mesure des températures en continu dans les cours d'eau de France",
            font=dict(color="#4169E1", size=20),
        ),
        height=600,
        width=1000,
    )

    return fig, selected_region, selected_dept


# Callback pour mettre à jour l'histogramme
@app.callback(
    Output(component_id="hist_annee", component_property="figure"),
    Input(component_id="range-slider-year", component_property="value"),
)
def update_histogram(selected_years):
    filtered_df = df[
        (df["annee_mise_en_service"] >= selected_years[0])
        & (df["annee_mise_en_service"] <= selected_years[1])
    ]
    histogram_fig = px.histogram(
        filtered_df,
        x="annee_mise_en_service",
        height=600,
        width=1000,
        color_discrete_sequence=["#2ecc71"],
    )

    histogram_fig.update_layout(
        title=dict(
            text="Nombre de stations par année de mise en service",
            font=dict(color="#e74c3c", size=20),
            x=0.5,
        )
    )
    return histogram_fig


# Lancement de l'application
if __name__ == "__main__":
    app.run_server(debug=True)
