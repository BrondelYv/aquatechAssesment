# importation des bibliothèques de manipulation et visualisation de données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# chargement de données sur les fuites d'eau par jour (échantillon de données)
leaks_per_day = pd.read_csv('result/leaks_per_day.csv')

# groupe par 'date' et 'sensor_addr' et compter le nombre de fuites
dfplot = leaks_per_day.groupby(['date', 'sensor_addr'])['total'].sum().reset_index()

dfplot = dfplot.sort_values('date')

# filtrons les 10 premiers jours
first_10_days = dfplot['date'].unique()[:10]
dfplot_first_10_days = dfplot[dfplot['date'].isin(first_10_days)]

# graphe fuite par jour et capteur
plt.figure(figsize=(12, 8))
ax = sns.barplot(x='date', y='total', hue='sensor_addr', data=dfplot_first_10_days, palette='Set2')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                xytext=(0, 5), textcoords='offset points')

# titres et labels
plt.title('total de fuites par jour et par capteur (10 premiers jours)')
plt.xlabel('Date')
plt.ylabel('Nombre de Fuites (L)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
