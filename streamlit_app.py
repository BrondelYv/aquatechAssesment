# importation des bibliothèques utiles pour lancer l'application streamlit
import pandas as pd
import streamlit as st
import plotly.express as px

# titre de l'application
st.title("Résultats Test de Recrutement AquaTech-Innovation")

# chargement des donnés importantes pour l'analyse
totals_df = pd.read_csv('result/totals.csv')
leaks_df = pd.read_csv('result/leaks.csv')
leaks_per_day_df = pd.read_csv('result/leaks_per_day.csv')

# vu total des consommations d'eau par capteur
st.subheader("Total des consommations d'eau en (L) par capteur")
st.dataframe(totals_df)

# graphe des top 20 capteurs par consommation totale
st.subheader("Top 20 capteurs par consommation totale")
top_20_consumption = totals_df.sort_values(by='total', ascending=False).head(20)  # Correction ici
fig1 = px.bar(top_20_consumption, x='sensor_addr', y='total', 
              labels={'sensor_addr': 'Capteur', 'total': 'Consommation Totale (L)'},
              title="Top 20 capteurs par consommation d'eau totale")
st.plotly_chart(fig1)

# vu total des fuites par capteur
st.subheader("Total des fuites d'eau (L) par capteur")
st.dataframe(leaks_df)

# graphe des top 20 capteurs par fuite d'eau tolal
st.subheader("Top 20 capteurs par totale des fuites d'eau (L)")
top_20_leaks = leaks_df.sort_values(by='total', ascending=False).head(20)  # Correction ici
fig2 = px.bar(top_20_leaks, x='sensor_addr', y='total', 
              labels={'sensor_addr': 'Capteur', 'total': 'Fuite Totale (L)'},
              title="Top 20 capteurs par totale des fuites d'eau (L)")
st.plotly_chart(fig2)

# vu de fuites d'eau par jour
st.subheader("Total des fuites par jour")
dfplot = leaks_per_day_df.groupby('date')['total'].sum().reset_index()
fig3 = px.bar(dfplot, x='date', y='total', 
              labels={'date': 'Date', 'total': 'Total des Fuites (L)'},
              title="Total des fuites par jour")
st.plotly_chart(fig3)

# vu de fuites d'eau par jour et par capteur (les 10 premiers jours)
st.subheader("Fuites par jour et par capteur (les 10 premiers jours)")
dfplot_sensor = leaks_per_day_df.groupby(['date', 'sensor_addr'])['total'].sum().reset_index()
first_10_days = dfplot_sensor['date'].unique()[:10]
dfplot_first_10_days = dfplot_sensor[dfplot_sensor['date'].isin(first_10_days)]

fig4 = px.bar(dfplot_first_10_days, x='date', y='total', color='sensor_addr', 
              labels={'date': 'Date', 'total': 'Total des Fuites (L)', 'sensor_addr': 'Capteur'},
              title="Fuites par jour et par capteur (10 premiers jours)")
st.plotly_chart(fig4)

# vu des fichiers CSV générés
st.subheader("Téléchargement des fichiers CSV attendus")

# télécharge le fichier totals.csv
st.download_button(
    label="Télécharger  totals.csv",
    data=open('result/totals.csv', 'rb'),
    file_name='totals.csv',
    mime='text/csv'
)

# télécharge le fichier leaks.csv
st.download_button(
    label="Télécharger  leaks.csv",
    data=open('result/leaks.csv', 'rb'),
    file_name='leaks.csv',
    mime='text/csv'
)

# télécharge le fichier leaks_per_day.csv
st.download_button(
    label="Télécharger  leaks_per_day.csv  (optionnel)",
    data=open('result/leaks_per_day.csv', 'rb'),
    file_name='leaks_per_day.csv',
    mime='text/csv'
)

# fin de l'analyse
st.title("Fin de l'analyse  - Merci pour votre attention.")
print('\n')
st.write("Yvell Mvoumbi")