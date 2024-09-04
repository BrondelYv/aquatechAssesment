# importation des bibliothèques de manipulation et visualisation de données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# chargement des données sur la fuite totale d'eau et les capteurs
leaks = pd.read_csv('result/leaks.csv')

# tri par la consommation totale en ordre décroissant
leaks = leaks.sort_values(by='total', ascending=False)

# top 20 capteurs avec la plus grande fuite
top_20_leaks = leaks.head(20)

# graphe top 20 capteurs par fuite
plt.figure(figsize=(12, 8))
ax = sns.barplot(x='sensor_addr', y='total', data=top_20_leaks, palette='Set2')

# étiquettes de données
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                xytext=(0, 5), textcoords='offset points')

# titres et labels
plt.title('Top 20 capteurs par fuite totale')
plt.xlabel('Capteur (sensor_addr)')
plt.ylabel('Fuite Totale (L)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()