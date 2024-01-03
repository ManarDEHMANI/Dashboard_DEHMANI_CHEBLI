# get_data.py
import pandas as pd
import requests


def station():
    df = pd.read_csv("data/stations_data.csv", encoding="latin1")
    df["annee_mise_en_service"] = pd.to_datetime(df["Annee"]).dt.year
    return df


def impact():
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/agribalyse-31-synthese/lines?page=1&after=1&size=2518"
    response = requests.get(url)
    data = response.json()
    dataf = pd.DataFrame(data["results"])
    return dataf
