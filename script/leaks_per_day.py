# importation des bibliothèques de manipulation et conversion des dates
import pandas as pd
import datetime as dt


# fonction ts_day qui transforme les timestamps en dates e.g. 2022-04-10
def ts_day(x):
	record_date = dt.date.fromtimestamp(float(str(x).replace(',', '.')))
	return record_date.isoformat()

# chargement des données sur la valeurs de consommations et leur timestamps
records_day = pd.read_csv('data/records.csv', sep=";")

# application de la fonction ts_day pour convertir la colonne timestamp en date iso
records_day['timestamp'] = records_day['timestamp'].apply(lambda x: ts_day(x))

# chargement des données des capteurs
sensors = pd.read_csv('data/sensors.csv', sep=";")

# fusion des données des capteurs avec les consommations avec une jointure à gauche
sensors_totals = pd.merge(sensors, records_day, left_on='sensor_addr', right_on='transmitter_addr', how='left')

# excluons les consommations avec une valeur nulle
sensors_totals = sensors_totals[sensors_totals['value'] != 0]

# récuprérons un echantillonnage de données aléatoire de 50.000 lignes, pour effectuer les tests et améliorer les performances
sensors_totals = sensors_totals.sample(n=50000, random_state=12)

# initialisons ces trois listes pour stocker les capteurs parents, quantités de fuites et les dates associées
parents = []
leaks = []
dates = []

for date in sensors_totals['timestamp'].unique():
	dfd = sensors_totals[sensors_totals['timestamp'] == date]

	for parent in sensors_totals['parent_addr'].unique():

		# vérifions si le parent n'est pas NaN
		if pd.notna(parent):

			# calculer le total des enfants directs
			children_total = dfd[dfd['parent_addr'] == parent]['value'].sum()

	        # calculer le total du parent
			parent_total = dfd[dfd['sensor_addr'] == parent]['value'].sum()

			# calculer la fuite (si le total des enfants est inférieur au total du parent)
			leak_amount = parent_total - children_total

			if leak_amount > 0:
				leaks.append(leak_amount)
				parents.append(parent)
				dates.append(date)


# création du dataframe au schéma requis
leaks_per_noded = pd.DataFrame({'sensor_addr': parents, 'total': leaks, 'date': dates})

# sauvergardons-le au format csv
leaks_per_noded.to_csv('result/leaks_per_day.csv', index=False)