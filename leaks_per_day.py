import pandas as pd
import datetime as dt

# transforme les timestamps en dates e.g. 2022-04-10
def ts_day(x):
	record_date = dt.date.fromtimestamp(float(str(x).replace(',', '.')))
	return record_date.isoformat()

records_day = pd.read_csv('data/records.csv', sep=";")

records_day['timestamp'] = records_day['timestamp'].apply(lambda x: ts_day(x))

sensors = pd.read_csv('data/sensors.csv', sep=";")

sensors_totals = pd.merge(sensors, records_day, left_on='sensor_addr', right_on='transmitter_addr', how='left')

parents = []
leaks = []
dates = []

for date in sensors_totals['timestamp'].unique():
	for parent in sensors_totals['parent_addr'].unique():
		# vérifier si le parent n'est pas NaN
		if pd.notna(parent):
			# calculer le total des enfants directs
			children_total = sensors_totals[(sensors_totals['parent_addr'] == parent) & (sensors_totals['timestamp'] == date)]['value'].sum()

	        # calculer le total du parent
			parent_total = sensors_totals[(sensors_totals['sensor_addr'] == parent) & (sensors_totals['timestamp'] == date)]['value'].sum()

			# calculer la fuite (si le total des enfants est inférieur au total du parent)
			leak_amount = parent_total - children_total

			if leak_amount > 0:
				leaks.append(leak_amount)
				parents.append(parent)

	dates.append(date)

# création du dataframe au schéma requis
leaks_per_noded = pd.DataFrame({'sensor_addr': parents, 'total': leaks, 'date': date})

# sauvergarde
leaks_per_noded.to_csv('result/leaks_per_day.csv', index=False)




