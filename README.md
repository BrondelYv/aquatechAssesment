# Test de recrutement développeur

## objectifs du projet
*Ce projet vise à analyser les données de consommation d'eau collectées par différents capteurs et à identifier les fuites d'eau totales par capteur et par jour.
Nous avons automatisé le processus des scripts en python et est divisé en plusieurs étapes*

1. totals.py aggrège les données de consommation d'eau par capteur.

2. leaks.py analyse les données aggrégées pour identifier les fuites en comparant la consommation totale des capteurs parents et de leurs capteurs enfants.

3. leaks_per_day.py analyse les fuites d'eau par jour et convertit les timestapms en dates ISO

4. display_leaks_per_day.py permet de visualiser les fuites d'au par jour

5. display_leaks_per_day_per_sensors.py visualise les fuites d'eau par jour et par capteur

6. top20_totals.py permet de visualiser les top 20 capteurs qui ont consommé plus de litre d'eau

7. top20_leaks.py visaulise les top 20 capteurs qui ont plus fuité en litre d'eau

## technologies
python : language simple d'accès connu pour ces librairies de data science en raison de sa syntaxe simple et riche en bibliothèques, flexible et facile à utilser. 

pandas : librairie indispensable pour la manipulation et traitement de données tabulaires en python, fournit des structures de données en DataFrames.

numpy : utilitaire pour le traitement de vecteur souvent utilisé conjointement avec pandas pour le calcul numérique et pour améliorer les performences lors de la manipulation des données volumineuses (Big Data).

matplotlib / seaborn : librairies de visualisation de données les plus connues et aident à comprendre les tendences et les anomalies dans les données.

plotly : une librairie de visualisation qui rende nos graphes plus intéractive et on peut sélectionner une partie de la visualisation pour mieux analyser les données. 

streamlit : pour visualiser les resultats du test via le port 8501, c'est une bibliothèque de python qui permet de créer des applications d'analyse de données ou de machine learning afin de faire des peésentations plus synthétiques.

Docker : plateforme de conteneurisation qui permet de créer, déployer et d'exécuter des applications dans un environnement isolé et bien gérer les les dépendences.
  
*Ces outils disposent d'une grande communauté ce qui permet de résoudre les problèmes récurents facilement.*

## dépendences et quelques bonnes pratiques

1. python doit être installé sur la machine de travail avec une version 3.8 ou supérieure (si ce n'est le cas)

2. Pour lancer l'application en dehors de docker, il est recommandé d'installer la liste des librairies python dans le fichier *requirements.txt*.
 * **python -m venv env** pour créer l'environnement virtuel
 * **env\Scripts\activate** pour activer l'environnement virtuel
 * **pip install -r requirements.txt** pour installer toutes les dépendences
 * on peut lancer nos fichier .py dans /script avec la commande : **python name_fichier.py** si dans result on n'a pas les données générées.
 * enfin on peut lancer l'application avec la commande : **streamlit run streamlit_app.py**

3. exécution avec docker, on doit s'assurer que docker est bien installé sur la machine de travail.

* avant de lancer docker on doit aussi s'assurer que la virtualisation est activée dans le BIOS de la machine.
on n'a pas besoin d'installer les dépendences python manuellement, les fichiers Dockerfile et compose.yaml s'occuperont de la configuration de l'environnement

* après installation de docker et activation de la virtualistaion, on peut vérifier la version de docker installé avec la commande **docker --version**

* par la suite on peut construire notre image docker à partir de notre fichier Dockerfile avec la commande **docker build -t name_image .**

* lancencement du conteneur à partir de l'image construite avec la commande **docker run name_image**

* une fois dans docker, il faut aller parametrer son port sur 8501 et ajouter le chemin **/result** afin d'écouter sur le localhost:8501:8501 pour voir les résultats du test.

* on peut voir les conteneurs actifs et inactifs avec la commande **docker ps -a** et on peut aussi arrêter l'exécution du conteneur qu'on souhaite avec la commande **docker-compose down 'conteneur_id'**.

## conventions

Les scripts de data science sont souvent court mais ils respectent tout de même des pratiques conventionnelles.
Par exemple, l'usage du snake_case et le cloisonement des datasets. Cela permet de minimiser les erreurs et de faciliter la gestion des données tout au long du processus de traitement.

## résultats

1. csv : deux fichiers csv (leaks.csv, totals.csv)

2. figure : quatre figures représentant <les fuites d'eau par jour>, <les fuites d'eau par jour et par capteur>, <les top 20 capteurs par total consommation d'eau> et <les top 20 capteurs par total fuite d'eau>.
