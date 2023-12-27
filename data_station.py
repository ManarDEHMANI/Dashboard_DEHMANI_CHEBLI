# Importation des modules nécessaires
import csv
import requests
import os

# Définition de l'URL de l'API
url = "https://hubeau.eaufrance.fr/api/v1/temperature/station"

# Envoi d'une requête GET à l'API
response = requests.get(url)
# Récupération de la réponse en format JSON
data = response.json()

# Initialisation d'une liste csv_data qui représente les noms des colonnes du fichier csv
csv_data = [["Latitude", "Longitude", "Station", "Departement", "Region", "Annee"]]

# Parcours des données de stations de l'API
for station in data["data"]:
    # Extraction des informations nécessaires
    latitude = station["latitude"]
    longitude = station["longitude"]
    station_name = station["libelle_station"]
    departement = station["libelle_departement"]
    region = station["libelle_region"]
    annee = station["date_mise_en_service"]
    # Exclusion des stations avec une région égale à %% (région non défini)
    if region != "%%":
        # Ajout des informations à la liste csv_data
        csv_data.append([latitude, longitude, station_name, departement, region, annee])

# Définition du chemin du fichier CSV de sortie
csv_file_path = os.path.join("data", "stations_data.csv")

# Ouverture du fichier CSV en mode lecture et écriture
with open(csv_file_path, "w+", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(csv_data)
