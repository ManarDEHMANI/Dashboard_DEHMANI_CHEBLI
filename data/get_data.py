# Importation des bibliothèques nécessaires
import pandas as pd
import requests


# Fonction pour récupérer les données de stations depuis un fichier CSV local
def station():
    # Charger le fichier CSV en utilisant pandas
    df = pd.read_csv("data/stations_data.csv", encoding="latin1")

    # Ajouter une colonne 'annee_mise_en_service' basée sur la colonne 'Annee' convertie en années
    df["annee_mise_en_service"] = pd.to_datetime(df["Annee"]).dt.year

    # Retourner le DataFrame résultant
    return df


# Fonction pour récupérer des données depuis une API externe (Ademe)
def produits():
    # URL de l'API Ademe
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/agribalyse-31-synthese/lines?page=1&after=1&size=2518"

    # Effectuer une requête HTTP GET pour obtenir les données de l'API
    response = requests.get(url)

    # Convertir la réponse JSON en DataFrame pandas
    data = response.json()
    dataf = pd.DataFrame(data["results"])

    # Retourner le DataFrame résultant
    return dataf


# Ensemble de valeurs souhaitées pour le sous-groupe, les aliments et les matériaux
desired_sous_group = {
    "herbes",
    "algues",
    "fruits",
    "poissons cuits",
    "gâteaux et pâtisseries",
    "céréales de petit-déjeuner et biscuits",
    "sauces",
    "épices",
    "ingrédients divers",
}
desired_aliments = {
    "fruits, légumes, légumineuses et oléagineux",
    "lait et produits laitiers",
    "aliments infantiles",
    "produits céréaliers",
    "entrées et plats composés",
    "viandes, œufs, poissons",
}
desired_materials = {"Verre", "Papier", "Carton", "Aluminium", "Pas d'emballage"}
