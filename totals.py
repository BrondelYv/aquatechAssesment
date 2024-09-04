# importation de la bibliothèque 'pandas' utile pour la manipualtion des données
import pandas as pd

# chargement des données sur la consommation d'eau
dfr = pd.read_csv('data/records.csv', sep=";")

# groupement des données par transmetteur
totals = dfr[['transmitter_addr', 'value']].groupby('transmitter_addr').sum()

# transformation de l'index en colonne pour simplifier la sauvegarde
totals = totals.reset_index()

# renommage des colonnes
totals.rename(columns={'transmitter_addr': 'sensor_addr', 'value': 'total'}, inplace=True)

# sauvegardons-le au format csv
totals.to_csv('result/totals.csv', index=False)