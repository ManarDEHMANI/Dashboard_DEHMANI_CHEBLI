# function.py
import dash
from data.get_data import (
    desired_aliments,
    desired_materials,
    desired_sous_group,
)
import plotly.express as px
import data.get_data

df = data.get_data.station()
dataf = data.get_data.produits()


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
        ),
        bargap=0.1,
    )
    return histogram_fig


def update_histogram_superficie(_):
    histogram_superficie_fig = px.histogram(
        df,
        x="Supercifie_Topographique",
        height=600,
        width=1000,
        color_discrete_sequence=["#3498db"],
    )

    histogram_superficie_fig.update_layout(
        title=dict(
            text="Distribution de la superficie topographique des stations",
            font=dict(color="#e74c3c", size=20),
            x=0.5,
        ),
        bargap=0.1,
    )
    return histogram_superficie_fig


def update_histogram_cout_energetique(selected_material):
    df_filtered = dataf[dataf["Matériau_d'emballage"].isin(desired_materials)]

    if selected_material and selected_material != "Tous":
        df_filtered = df_filtered[
            df_filtered["Matériau_d'emballage"] == selected_material
        ]

    histogram_cout_energetique = px.histogram(
        df_filtered,
        x="Score_unique_EF",
        color="Matériau_d'emballage",
        nbins=30,
        barmode="group",
    )

    title_text = (
        "Impact Environnemental des Matériaux d'Emballage Évalué par le Score Unique EF"
    )
    if selected_material and selected_material != "Tous":
        title_text += f" : {selected_material}"

    histogram_cout_energetique.update_layout(
        title=dict(
            text=title_text,
            font=dict(color="#e74c3c", size=20),
            x=0.5,
        ),
        bargap=0.1,
    )

    return histogram_cout_energetique


def update_histogram_eutrophisation_sol(selected_group):
    df_filtered = dataf[dataf["Groupe_d'aliment"].isin(desired_aliments)]

    if selected_group and selected_group != "Tous":
        df_filtered = df_filtered[df_filtered["Groupe_d'aliment"] == selected_group]

    title_text = "Relation entre l'Eutrophisation Terrestre et l'Utilisation du Sol"
    if selected_group and selected_group != "Tous":
        title_text += f"={selected_group}"

    histogram_eutrophisation_sol = px.histogram(
        df_filtered,
        x="Eutrophisation_terrestre",
        y="Utilisation_du_sol",
        nbins=30,
        color="Groupe_d'aliment",
        title=title_text,
        barmode="group",
    )

    histogram_eutrophisation_sol.update_layout(
        title=dict(
            font=dict(color="#e74c3c", size=20),
            x=0.5,
        ),
        bargap=0.1,
    )

    return histogram_eutrophisation_sol


def update_histogram_impact_climat_ozone(selected_sous_group):
    df_filtered = dataf[dataf["Sous-groupe_d'aliment"].isin(desired_sous_group)]

    if selected_sous_group and selected_sous_group != "Tous":
        df_filtered = df_filtered[
            df_filtered["Sous-groupe_d'aliment"] == selected_sous_group
        ]

    title_text = "Changement Climatique vs. Impact sur la Couche d'Ozone"
    if selected_sous_group and selected_sous_group != "Tous":
        title_text += f"={selected_sous_group}"

    histogram_climat_ozone = px.histogram(
        df_filtered,
        x="Changement_climatique",
        y="Appauvrissement_de_la_couche_d'ozone",
        color="Sous-groupe_d'aliment",
        title=title_text,
        barmode="group",
    )

    histogram_climat_ozone.update_layout(
        title=dict(
            font=dict(color="#e74c3c", size=20),
            x=0.5,
        ),
        bargap=0.1,
    )

    return histogram_climat_ozone
