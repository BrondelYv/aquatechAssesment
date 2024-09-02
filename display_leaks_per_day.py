import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

leaks_per_day = pd.read_csv('result/leaks_per_day.csv')


dfplot = leaks_per_day.groupby('date')['total'].sum()

sns.barplot(dfplot, palette='Set2')

plt.title('Pertes en litre d\'eau par jour')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()