# importation des bibliothèques de manipulation et visualisation de données
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# chargement de données sur les fuites d'eau par jour (échantillon de données)
leaks_per_day = pd.read_csv('result/leaks_per_day.csv')

# regroupons la quantité totale de fuite par date
dfplot = leaks_per_day.groupby('date')['total'].sum()

# graphe en barre fuite d'eau par jour
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=dfplot.index, y=dfplot.values, palette='Set2')

# étiquettes sur les barres
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                xytext=(0, 5), textcoords='offset points')

plt.title('Pertes en litre d\'eau par jour')
plt.xlabel('Date')
plt.ylabel('Total des Fuites (L)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig('result/leaks_per_day_plot.png')
plt.show()