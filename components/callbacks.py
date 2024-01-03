# callbacks.py
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html, dcc
import pandas as pd
from app import app
from components.function import (
    update_map_and_selectors,
    update_histogram,
    update_histogram_superficie,
    update_histogram_cout_energetique,
)
from data.get_data import station
import plotly.express as px

df = station()

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
dept_dropdown = dcc.Dropdown(
    id="dept-dropdown",
    options=dept_options,
    value="Tous",
    clearable=False,
    style={"width": "50%", "margin": "auto"},
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
    data_map = update_map_and_selectors(selected_region, selected_dept)
    return data_map


@app.callback(
    Output(component_id="hist_annee", component_property="figure"),
    Input(component_id="range-slider-year", component_property="value"),
)
def histo_year(selected_years):
    data_year = update_histogram(selected_years)
    return data_year


@app.callback(
    Output(component_id="hist_superficie", component_property="figure"),
    # Ne pas utiliser selected_years pour filtrer les données
    Input(component_id="hist_superficie", component_property="figure"),
)
def histo_superficie(_):
    data_supercifie = update_histogram_superficie(_)
    return data_supercifie


@app.callback(
    Output(component_id="cout_energetique", component_property="figure"),
    # Ne pas utiliser selected_years pour filtrer les données
    Input(component_id="cout_energetique", component_property="figure"),
)
def histo_cout_energetique(_):
    data_cout_energetique = update_histogram_cout_energetique(_)
    return data_cout_energetique
