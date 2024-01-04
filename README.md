# Dashboard Environnemental

## Table des matières

- [Description](#description)
- [Guide de l'utilisateur](#guide-de-lutilisateur)
- [Rapport d'analyse](#rapport-danalyse)
- [Guide du développeur](#guide-de-développeur)

## Description

Le Dashboard Environnemental est un projet visant à fournir une expérience interactive pour explorer des données environnementales à l'aide de représentations graphiques dynamiques. Ce dashboard utilise les données provenant des API Hubeau et API Agribalyse.

## Guide de l'utilisateur

Pour déployer et utiliser ce dashboard sur une votre machine, suivez les étapes ci-dessous :

1. Clonez le dépôt en utilisant la commande suivante :

   ```bash
   git clone https://github.com/ManarDEHMANI/Dashboard_DEHMANI_CHEBLI.git
   ```

2. Accédez au dossier du projet :

   ```bash
   cd Dashboard_DEHMANI_CHEBLI
   ```

3. Installez les dépendances à l'aide de la commande :

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Lancez l'application avec :

   ```bash
   python main.py
   ```

5. Ouvrez votre navigateur et accédez à [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

6. Vous devriez maintenant voir Dashboard et pouvoir interagir avec ses fonctionnalités.

## Rapport d'analyse

### Introduction

Le Dashboard Environnemental s'appuie sur les données des API Hubeau et API Agribalyse pour offrir une vue approfondie des données environnementales. Cette section du rapport fournira des insights clés extraits de l'analyse des données.

### Données Utilisées

#### 1. API Hub'Eau - Température des cours d'eau

L'API Hub'Eau - Température des cours d'eau offre une source riche de données sur les températures mesurées dans les cours d'eau de France métropolitaine. En se concentrant sur l'opération "station", nous avons pu rechercher les stations où les températures sont mesurées en continu. Cela nous permet d'obtenir des informations détaillées sur les variations de température dans différentes régions.

[Documentation API Hub'Eau - Température des cours d'eau](https://api.gouv.fr/documentation/api_hubeau_temperature_rivieres)

#### 2. API Impacts environnementaux - AGRIBALYSE

L'API Impacts environnementaux - AGRIBALYSE, fournie par l'ADEME, nous offre des indicateurs d'impacts environnementaux pour les produits agricoles et alimentaires en France. En utilisant cette API, nous avons pu explorer les impacts écologiques de la production alimentaire, tels que les émissions de gaz à effet de serre, le coût énergétique, etc.

[Documentation API Impacts environnementaux - AGRIBALYSE](https://api.gouv.fr/documentation/api_agribalyse)

### Dashboard

### 1. Carte de localisation :

La carte de localisation offre une vue d'ensemble des stations de mesure de température des cours d'eau en France. Cette représentation visuelle permet d'identifier rapidement les zones géographiques où les stations sont concentrées.Ainsi nous avons mis en place que la carte peut être dynamique et offre une libérté de filtrage par département ou région offre une flexibilité d'exploration, permettant aux utilisateurs de se concentrer sur des zones spécifiques.

_Filtrage par Département:_ En utilisant ce filtre, les utilisateurs peuvent restreindre la visualisation aux stations présentes dans un département spécifique. Cela s'avère utile pour une analyse plus détaillée au niveau local.

_Filtrage par Région:_ Le filtre par région offre une perspective plus large, permettant de comparer les températures des cours d'eau entre différentes régions. Cela peut aider à identifier des tendances ou des disparités régionales.

### 2. Histogrammes :

#### 2.1 Histogramme de nombre de station par année de mise en service :

L'histogramme présente le nombre de stations de mesure environnementale en fonction de leur année de mise en service. Cette visualisation permet d'analyser l'évolution de l'implantation des stations sur une période donnée.

- **Axe horizontal (abscisse) :** Années de mise en service des stations de mesure.
- **Axe vertical (ordonnée) :** Nombre de stations mises en service chaque année.
- **Barres :** Chaque barre correspond à une période spécifique, approximativement une décennie.

En effet, l'histogramme montre également une fonctionnalité interactive : **l'utilisation de sélecteurs** pour choisir un intervalle d'années. Cette option permet aux utilisateurs d'affiner leur analyse en se concentrant sur des périodes spécifiques.

Après avoir analyser le résultat de cet histogramme, on peut conclure une forte mise en place de stations de mesure environnementale au début du XXe siècle, suivie d'une diminution jusqu'aux années 2000 où l'on observe une nouvelle augmentation significative. Cette tendance reflète probablement l'engagement envers la surveillance environnementale a fluctué au fil du temps, avec une attention renouvelée dans les années 2000.

#### 2.2 Histogramme de distribution de la supercifie topographique des stations :

#### 2.3 :

### 2.4 :

### 2.5 :

### Guide du développeur
