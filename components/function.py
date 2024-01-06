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

# Common title style for all figures
title_style = {"font": {"color": "#4169E1", "size": 20}, "x": 0.5}

common_layout = {
    "bargap": 0.1,
    "paper_bgcolor": "rgba(51, 51, 51, 1)",
    "plot_bgcolor": "rgba(51, 51, 51, 1)",
    "legend": {
        "font": {
            "size": 12,  # Augmenter cette valeur pour une plus grande taille de légende
            "color": "#ADD8E6",
        },
        "bgcolor": "rgba(51, 51, 51, 1)",
    },
    "xaxis": {
        "title_font": {
            "size": 16,
            "color": "#D2691E",
        },  # Définissez la couleur du titre de l'axe
        "tickfont": {
            "size": 14,
            "color": "#FFFFFF",
        },  # Définissez la couleur des étiquettes de l'axe
        "tickcolor": "#FFFFFF",  # Définissez la couleur des ticks de l'axe
        "linecolor": "#FFFFFF",  # Définissez la couleur de la ligne de l'axe
        "gridcolor": "#555555",  # Définissez une couleur de grille plus discrète si nécessaire
        # ... autres propriétés de l'axe ...
    },
    "yaxis": {
        "title_font": {"size": 16, "color": "#D2691E"},  # Même chose pour l'axe des y
        "tickfont": {"size": 14, "color": "#FFFFFF"},
        "tickcolor": "#FFFFFF",
        "linecolor": "#FFFFFF",
        "gridcolor": "#555555",
        # ... autres propriétés de l'axe ...
    },
}


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
        title="Stations de mesure des températures en continu dans les cours d'eau de France",
    )
    fig.update_layout(
        mapbox=dict(
            center=dict(lat=46.6031, lon=1.8883),
            style="open-street-map",
            zoom=5,
        ),
        height=600,
        width=1000,
        title=title_style,
        paper_bgcolor="#333333",
        plot_bgcolor="#333333",
        legend=dict(
            font=dict(color="#ADD8E6"),  # Marron terreux pour le texte de la légende
        ),
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
        title="Nombre de stations par année de mise en service",
    )
    combined_layout = {
        **common_layout,
        "title": {
            "text": "Nombre de stations par année de mise en service",  # Apply title text
            **title_style,  # Apply title style settings
        },
    }
    histogram_fig.update_layout(**combined_layout)
    return histogram_fig


def update_histogram_superficie(_):
    histogram_superficie_fig = px.histogram(
        df,
        x="Supercifie_Topographique",
        height=600,
        width=1000,
        color_discrete_sequence=["#3498db"],
    )
    combined_layout = {
        **common_layout,
        "title": {
            "text": "Distribution de la supercifie topographique des stations",  # Apply title text
            **title_style,  # Apply title style settings
        },
    }
    histogram_superficie_fig.update_layout(**combined_layout)
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
    combined_layout = {
        **common_layout,  # Apply common layout settings
        "title": {
            "text": title_text,  # Apply title text
            **title_style,  # Apply title style settings
        },
    }

    # Apply the combined layout to the histogram
    histogram_cout_energetique.update_layout(**combined_layout)

    return histogram_cout_energetique


def update_histogram_eutrophisation_sol(selected_group):
    df_filtered = dataf[dataf["Groupe_d'aliment"].isin(desired_aliments)]

    if selected_group and selected_group != "Tous":
        df_filtered = df_filtered[df_filtered["Groupe_d'aliment"] == selected_group]

    title_text = "Relation entre l'Eutrophisation Terrestre et l'Utilisation du Sol"
    histogram_eutrophisation_sol = px.histogram(
        df_filtered,
        x="Eutrophisation_terrestre",
        y="Utilisation_du_sol",
        nbins=30,
        color="Groupe_d'aliment",
        title=title_text,
        barmode="group",
    )

    combined_layout = {
        **common_layout,  # Apply common layout settings
        "title": {
            "text": title_text,  # Apply title text
            **title_style,  # Apply title style settings
        },
    }

    histogram_eutrophisation_sol.update_layout(**combined_layout)

    return histogram_eutrophisation_sol


def update_histogram_impact_climat_ozone(selected_sous_group):
    df_filtered = dataf[dataf["Sous-groupe_d'aliment"].isin(desired_sous_group)]

    if selected_sous_group and selected_sous_group != "Tous":
        df_filtered = df_filtered[
            df_filtered["Sous-groupe_d'aliment"] == selected_sous_group
        ]

    title_text = "Influence des Sous-groupes Alimentaires sur le Changement Climatique et l'Appauvrissement de la Couche d'Ozone"
    if selected_sous_group and selected_sous_group != "Tous":
        title_text += f":{selected_sous_group}"

    histogram_climat_ozone = px.histogram(
        df_filtered,
        x="Changement_climatique",
        y="Appauvrissement_de_la_couche_d'ozone",
        color="Sous-groupe_d'aliment",
        title=title_text,
        barmode="group",
    )

    combined_layout = {
        **common_layout,
        "title": {
            "text": title_text,  # Apply title text
            **title_style,  # Apply title style settings
        },
    }
    histogram_climat_ozone.update_layout(**combined_layout)
    return histogram_climat_ozone
