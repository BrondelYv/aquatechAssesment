# importation de la bibliothèque 'pandas' utile pour la manipualtion des données
import pandas as pd

# chargement des données sur la consommation totale d'eau et les capteurs
totals = pd.read_csv('result/totals.csv')
sensors = pd.read_csv('data/sensors.csv', sep=";")

# fusion des datasets afin de réaliser une étude multivariée
sensors_totals = pd.merge(sensors, totals, left_on='sensor_addr', right_on='sensor_addr', how='left')

# initialisons ces deux listes stocker les capteurs parents et leurs quantités de fuite détectée
parents = []
leaks = []

for parent in sensors_totals['parent_addr'].unique():
    # considérons tous les compteurs qui ne sont pas le compteur général

    if pd.notna(parent):

        # calculons le total des enfants directs
        children_total = sensors_totals[sensors_totals['parent_addr'] == parent]['total'].sum()

        # calculons le total du parent
        parent_total = sensors_totals[sensors_totals['sensor_addr'] == parent]['total'].values[0]

        # calculons la fuite (si le total des enfants est inférieur au total du parent)
        leak_amount = parent_total - children_total

        if leak_amount > 0:
            leaks.append(leak_amount)
            parents.append(parent)


# création du dataframe au schéma requis
leaks_per_node = pd.DataFrame({'sensor_addr': parents, 'total': leaks})

# sauvergardons-le au format csv
leaks_per_node.to_csv('result/leaks.csv', index=False)