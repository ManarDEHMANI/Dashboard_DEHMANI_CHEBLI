# callbacks.py
import components.function
import data.get_data
from dash.dependencies import Input, Output
from dash import dcc
from app import app

df = data.get_data.station()
dataf = data.get_data.produits()

region_options = [{"label": "Toutes les Régions", "value": "Toutes"}] + [
    {"label": r, "value": r} for r in df["Region"].unique()
]
dept_options = [{"label": "Tous les Départements", "value": "Tous"}] + [
    {"label": d, "value": d} for d in df["Departement"].unique()
]
materiaux_options = [{"label": "Tous les matériaux d'emballlages", "value": "Tous"}] + [
    {"label": m, "value": m} for m in data.get_data.desired_materials
]
group_options = [{"label": "Tous les groupes d'aliments", "value": "Tous"}] + [
    {"label": g, "value": g} for g in data.get_data.desired_aliments
]

sous_group_options = [
    {"label": "Tous les sous groupes d'aliments", "value": "Tous"}
] + [{"label": sous_g, "value": sous_g} for sous_g in data.get_data.desired_sous_group]

# Création des dropdowns pour sélectionner une région et un département
region_dropdown = dcc.Dropdown(
    id="region-dropdown",
    options=region_options,
    value="Toutes",
    clearable=False,
    style={
        "width": "50%",
        "margin": "auto",
    },
)
dept_dropdown = dcc.Dropdown(
    id="dept-dropdown",
    options=dept_options,
    value="Tous",
    clearable=False,
    style={
        "width": "50%",
        "margin": "auto",
    },
)
material_dropdown = dcc.Dropdown(
    id="material-dropdown",
    options=materiaux_options,
    value="Tous",
    clearable=False,
    style={
        "width": "50%",
        "margin": "auto",
    },
)

group_dropdown = dcc.Dropdown(
    id="groupe-dropdown",
    options=group_options,
    value="Tous",
    clearable=False,
    style={
        "width": "50%",
        "margin": "auto",
    },
)

sous_group_dropdown = dcc.Dropdown(
    id="sous_groupe-dropdown",
    options=sous_group_options,
    value="Tous",
    clearable=False,
    style={
        "width": "50%",
        "margin": "auto",
    },
)
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
def maps(selected_region, selected_dept):
    data_map = components.function.update_map_and_selectors(
        selected_region, selected_dept
    )
    return data_map


@app.callback(
    Output(component_id="hist_annee", component_property="figure"),
    Input(component_id="range-slider-year", component_property="value"),
)
def histo_year(selected_years):
    data_year = components.function.update_histogram(selected_years)
    return data_year


@app.callback(
    Output(component_id="hist_superficie", component_property="figure"),
    # Ne pas utiliser selected_years pour filtrer les données
    Input(component_id="hist_superficie", component_property="figure"),
)
def histo_superficie(_):
    data_supercifie = components.function.update_histogram_superficie(_)
    return data_supercifie


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


@app.callback(
    Output(component_id="impact-climat-utilisation-sol", component_property="figure"),
    # Ne pas utiliser selected_years pour filtrer les données
    Input(component_id="groupe-dropdown", component_property="value"),
)
def histo_eutrophisation_sol(selected_group):
    data_climat_sol = components.function.update_histogram_eutrophisation_sol(
        selected_group
    )
    return data_climat_sol


@app.callback(
    Output(component_id="impact-climat-ozone", component_property="figure"),
    Input(component_id="sous_groupe-dropdown", component_property="value"),
)
def histo_impact_climat_ozone(selected_sous_group):
    data_climat_ozone = components.function.update_histogram_impact_climat_ozone(
        selected_sous_group
    )
    return data_climat_ozone


@app.callback(
    Output("animated-text", "children"),
    Input("interval-component", "n_intervals"),
)
def update_text(n):
    text_list = [
        "Bienvenue sur le tableau de bord environnemental!",
        "Explorez les données pour découvrir des informations intéressantes.",
        "Commencez votre voyage maintenant!",
    ]
    return text_list[n % len(text_list)]
