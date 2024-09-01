import pandas as pd


dfr = pd.read_csv('data/records.csv', sep=";")

# groupement des données par transmetteur
totals = dfr[['transmitter_addr', 'value']].groupby('transmitter_addr').sum()

# transformation de l'index en colonne pour simplifier la sauvegarde
totals = totals.reset_index()

# renommage des colonnes
totals.rename(columns={'transmitter_addr': 'sensor_addr', 'value': 'total'}, inplace=True)

# sauvegarde
totals.to_csv('result/totals.csv', index=False)