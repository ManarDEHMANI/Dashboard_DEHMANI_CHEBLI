# Importations nécessaires pour utiliser les fonctionnalités de Dash et Plotly
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html, dcc

# Importations de modules locaux
import components.function
import data.get_data
from app import app

# Récupération des données nécessaires pour les sélecteurs (dropdown)
df = data.get_data.station()
dataf = data.get_data.produits()

dropdown_style = {
    "width": "50%",
    "margin": "auto",  # Blanc pour le texte
}
# Création des options pour les sélecteurs de région et département à partir des données uniques
region_options = [{"label": "Toutes les Régions", "value": "Toutes"}] + [
    {"label": r, "value": r} for r in df["Region"].unique()
]
dept_options = [{"label": "Tous les Départements", "value": "Tous"}] + [
    {"label": d, "value": d} for d in df["Departement"].unique()
]

# Création des options pour les sélecteurs de matériaux et de groupes d'aliments à partir des données souhaitées
materiaux_options = [{"label": "Tous les matériaux d'emballlages", "value": "Tous"}] + [
    {"label": m, "value": m} for m in data.get_data.desired_materials
]
group_options = [{"label": "Tous les groupes d'aliments", "value": "Tous"}] + [
    {"label": g, "value": g} for g in data.get_data.desired_aliments
]
sous_group_options = [
    {
        "label": "Tous les sous groupes d'aliments",
        "value": "Tous",
    }
] + [{"label": sous_g, "value": sous_g} for sous_g in data.get_data.desired_sous_group]

# Création des sélecteurs (dropdown) pour le choix des régions, départements, matériaux, groupes et sous-groupes d'aliments
region_dropdown = dcc.Dropdown(
    id="region-dropdown",
    options=region_options,
    value="Toutes",
    clearable=False,
    style=dropdown_style,
)
dept_dropdown = dcc.Dropdown(
    id="dept-dropdown",
    options=dept_options,
    value="Tous",
    clearable=False,
    style=dropdown_style,
)
material_dropdown = dcc.Dropdown(
    id="material-dropdown",
    options=materiaux_options,
    value="Tous",
    clearable=False,
    style=dropdown_style,
)

group_dropdown = dcc.Dropdown(
    id="groupe-dropdown",
    options=group_options,
    value="Tous",
    clearable=False,
    style=dropdown_style,
)

sous_group_dropdown = dcc.Dropdown(
    id="sous_groupe-dropdown",
    options=sous_group_options,
    value="Tous",
    clearable=False,
    style=dropdown_style,
)
# Création d'un RangeSlider pour le choix de l'année avec des marques spécifiques
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


# Définition des callbacks pour la mise à jour des figures en fonction des sélections de l'utilisateur
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
# Appel à la focntion update_map_and_selectors
def maps(selected_region, selected_dept):
    data_map = components.function.update_map_and_selectors(
        selected_region, selected_dept
    )
    return data_map


# Callback pour mettre à jour l'histogramme du nombre de station par année mise en service en fonction de la sélection sur le RangeSlider
@app.callback(
    Output(component_id="hist_annee", component_property="figure"),
    Input(component_id="range-slider-year", component_property="value"),
)
def histo_year(selected_years):
    data_year = components.function.update_histogram(selected_years)
    return data_year


# Callback pour la mise à jour de l'histogramme de la superficie topographique
@app.callback(
    Output(component_id="hist_superficie", component_property="figure"),
    Input(component_id="hist_superficie", component_property="figure"),
)
def histo_superficie(_):
    data_supercifie = components.function.update_histogram_superficie(_)
    return data_supercifie


# Callback pour la mise à jour de l'histogramme du coût énergétique en fonction du matériau sélectionné
@app.callback(
    Output(component_id="score_material", component_property="figure"),
    # Ne pas utiliser selected_years pour filtrer les données
    Input(component_id="material-dropdown", component_property="value"),
)
def histo_cout_energetique(selected_material):
    data_cout_energetique = components.function.update_histogram_cout_energetique(
        selected_material
    )
    return data_cout_energetique


# Callback pour la mise à jour de l'histogramme de la relation entre l'eutrophisation terrestre et l'utilisation du sol en fonction du group sélectionné
@app.callback(
    Output(component_id="utilisation-sol", component_property="figure"),
    Input(component_id="groupe-dropdown", component_property="value"),
)
def histo_eutrophisation_sol(selected_group):
    data_climat_sol = components.function.update_histogram_eutrophisation_sol(
        selected_group
    )
    return data_climat_sol


# Callback pour la mise à jour de l'histogramme d'influence des Sous-groupes Alimentaires sur le Changement Climatique et l'Appauvrissement de la Couche d'Ozone en fonction du sous group sélectionné


@app.callback(
    Output(component_id="impact-climat-ozone", component_property="figure"),
    Input(component_id="sous_groupe-dropdown", component_property="value"),
)
def histo_impact_climat_ozone(selected_sous_group):
    data_climat_ozone = components.function.update_histogram_impact_climat_ozone(
        selected_sous_group
    )
    return data_climat_ozone


# Callback pour la mise à jour du texte animé sur la page d'accueil
@app.callback(
    Output("animated-text", "children"),
    Input("interval-component", "n_intervals"),
)
def update_text(n):
    # Liste des textes à afficher de manière cyclique
    text_list = [
        "Bienvenue sur le tableau de bord environnemental!",
        "Explorez les données pour découvrir des informations intéressantes.",
        "Commencez votre voyage maintenant!",
    ]
    # La fonction retourne un texte de la liste en fonction du compteur de l'Interval
    return text_list[n % len(text_list)]
