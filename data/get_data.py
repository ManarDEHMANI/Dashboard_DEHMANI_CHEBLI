# get_data.py
import pandas as pd


def station():
    df = pd.read_csv("data/stations_data.csv", encoding="latin1")
    df["annee_mise_en_service"] = pd.to_datetime(df["Annee"]).dt.year
    return df
