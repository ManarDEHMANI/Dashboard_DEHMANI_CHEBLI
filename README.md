# Dashboard Environnemental

## Table des Matières

- [Introduction](#introduction)
- [Guide de l'utilisateur](#guide-de-lutilisateur)
- [Rapport d'analyse](#rapport-danalyse)
  - [Données Utilisées](#donn\u00e9es-utilis\u00e9es)
    - [API Hub'Eau - Température des cours d'eau](#api-hubeau---temp\u00e9rature-des-cours-deau)
    - [API Impacts environnementaux - AGRIBALYSE](#api-impacts-environnementaux---agribalyse)
  - [Visualisations du Dashboard](#visualisations-du-dashboard)
    - [Carte de localisation](#carte-de-localisation)
    - [Histogrammes](#histogrammes)
      - [Histogramme de nombre de stations par année de mise en service](#histogramme-de-nombre-de-stations-par-ann\u00e9e-de-mise-en-service)
      - [Histogramme de distribution de la superficie topographique des stations](#histogramme-de-distribution-de-la-superficie-topographique-des-stations)
      - [Histogramme Impact Environnemental des Matériaux d'Emballage Évalué par le Score Unique EF](#histogramme-impact-environnemental-des-mat\u00e9riaux-demballage-\u00e9valu\u00e9-par-le-score-unique-ef)
      - [Histogramme Relation entre l'Eutrophisation Terrestre et l'Utilisation du Sol](#histogramme-relation-entre-leutrophisation-terrestre-et-lutilisation-du-sol)
      - [Histogramme Influence des Sous-groupes Alimentaires sur le Changement Climatique et l'Appauvrissement de la Couche d'Ozone](#histogramme-influence-des-sous-groupes-alimentaires-sur-le-changement-climatique-et-lappauvrissement-de-la-couche-dozone)
- [Guide du développeur](#guide-du-d\u00e9veloppeur)

## Introduction

Le Dashboard Environnemental est un projet visant à fournir une expérience interactive pour explorer des données environnementales de la France à l'aide de représentations graphiques dynamiques, offrant des analyses sur les cours d'eau et les impacts écologiques de la production alimentaire.

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

### Données Utilisées

#### 1. API Hub'Eau - Température des cours d'eau

L'API Hub'Eau - Température des cours d'eau offre une source riche de données sur les températures mesurées dans les cours d'eau de France métropolitaine. En se concentrant sur l'opération "station", nous avons pu rechercher les stations où les températures sont mesurées en continu. Cela nous permet d'obtenir des informations détaillées sur les variations de température dans différentes régions.

[Documentation API Hub'Eau - Température des cours d'eau](https://api.gouv.fr/documentation/api_hubeau_temperature_rivieres)

#### 2. API Impacts environnementaux - AGRIBALYSE

L'API Impacts environnementaux - AGRIBALYSE, fournie par l'ADEME, nous offre des indicateurs d'impacts environnementaux pour les produits agricoles et alimentaires en France. En utilisant cette API, nous avons pu explorer les impacts écologiques de la production alimentaire, tels que les émissions de gaz à effet de serre, le coût énergétique, etc.

[Documentation API Impacts environnementaux - AGRIBALYSE](https://api.gouv.fr/documentation/api_agribalyse)

### Visualisations du Dashboard

### 1. Carte de localisation :

La carte de localisation offre une vue d'ensemble des stations de mesure de température des cours d'eau en France. Cette représentation visuelle permet d'identifier rapidement les zones géographiques où les stations sont concentrées.Ainsi nous avons mis en place que la carte peut être dynamique et offre une libérté de filtrage par département ou région offre une flexibilité d'exploration, permettant aux utilisateurs de se concentrer sur des zones spécifiques.

_Filtrage par Département:_ En utilisant ce filtre, les utilisateurs peuvent restreindre la visualisation aux stations présentes dans un département spécifique. Cela s'avère utile pour une analyse plus détaillée au niveau local.

_Filtrage par Région:_ Le filtre par région offre une perspective plus large, permettant de comparer les températures des cours d'eau entre différentes régions. Cela peut aider à identifier des tendances ou des disparités régionales.

### 2. Histogrammes :

#### 2.1 Histogramme de nombre de station par année de mise en service :

L'histogramme présente le nombre de stations de mesure de température des cours d'eau en France en fonction de leur année de mise en service. Cette visualisation permet d'analyser l'évolution de l'implantation des stations sur une période donnée.

- **Axe horizontal (abscisse) :** Années de mise en service des stations de mesure.
- **Axe vertical (ordonnée) :** Nombre de stations mises en service chaque année.
- **Barres :** Chaque barre correspond à une période spécifique, approximativement une décennie.

En effet, l'histogramme montre également une fonctionnalité interactive : **l'utilisation de sélecteurs** pour choisir un intervalle d'années. Cette option permet aux utilisateurs d'affiner leur analyse en se concentrant sur des périodes spécifiques.

Après avoir analyser le résultat de cet histogramme, on peut conclure une forte mise en place de stations de mesure environnementale au début du XXe siècle, suivie d'une diminution jusqu'aux années 2000 où l'on observe une nouvelle augmentation significative. Cette tendance reflète probablement l'engagement envers la surveillance environnementale a fluctué au fil du temps, avec une attention renouvelée dans les années 2000.

#### 2.2 Histogramme de distribution de la supercifie topographique des stations :

Cet histogramme montre la distribution des superficies topographiques des stations de mesure de température des cours d'eau en France.

- **Axe horizontal (abscisse) :** Représente les catégories de superficies topographiques des stations, allant de 0 à plus de 10 000 unités
- **Axe vertical (ordonnée) :** Indique le nombre de stations qui entrent dans chaque catégorie de superficie.
- **Barres :** Chaque barre correspond à une plage de superficie spécifique.

En analysant, on peut conclure qu'il y a une prédominance des petites stations et une raréfaction des grandes installations, suggérant que les stations sont généralement conçues pour être économiques en espace et adaptatives c-à-d les stations plus petites peuvent être plus facilement intégrées dans divers environnements, y compris les zones urbaines ou restreintes.

#### 2.3 : Histogramme Impact Environnemental des Matériaux d'Emballage Évalué par le Score Unique EF

Cet hitogramme illustre l'impact environnemental des matériaux d'emballage, mesuré par le score unique EF.

- **Axe horizontal (Score unique EF):** Affiche les valeurs de l'impact environnemental pour les différents
- **Axe vertical (count):** Montre le nombre de fois qu'une certaine valeur de score EF a été enregistrée.
- **Barres**: Chaque barre de couleur différente représente un matériau d'emballage distinct, tel que le verre, le carton, l'aluminium, le papier, et l'option de ne pas utiliser d'emballage.

On note que Le score unique EF : Ce score reflète l'impact global d'un produit ou d'un service sur l'environnement, conformément aux directives établies par la Commission Européenne.

Par conséquent on peut déduire que l'histogramme permet d'identifier les matériaux d'emballage qui sont les plus durables et à promouvoir leur utilisation pour minimiser l'impact environnemental des produits. Il semble que l'option 'Pas d'emballage' soit celle qui présente le plus souvent les scores EF les plus bas, ce qui suggère que réduire ou éliminer l'emballage pourrait être la stratégie la plus favorable à l'environnement.

#### 2.4 : Histogramme Relation entre l'eutrophisation terrestre et l'utilisation du sol

L'histogramme montre la relation entre l'eutrophisation terrestre et l'utilisation du sol par différents groupes d'aliments. L'eutrophisation terrestre est définie comme un enrichissement excessif des sols en nutriments, particulièrement en azote, qui peut perturber l'équilibre écologique et conduire à un appauvrissement de la biodiversité, affectant surtout les sols agricoles.

- **L'axe horizontal :** Mesure l'indice d'eutrophisation terrestre pour les produits alimentaires,basé sur la quantité de nutriments ajoutés au sol par unité de production.
- **L'axe vertical :** Indique la somme de l'utilisation du sol, reflétant la quantité de terre utilisée pour produire ces aliments.
- **Les barres colorées :** représentent différents groupes d'aliments et leur impact combiné sur l'eutrophisation et l'utilisation du sol.

Après l'étude du résultat obtenue par l'histogramme,nous pouvons conclure qu'une barre haute sur l'histogramme indique qu'un groupe d'aliments spécifique a un impact relativement élevé sur l'eutrophisation terrestre et requiert une grande utilisation du sol pour sa production. Cela peut inciter à réfléchir sur les méthodes de production agricole et sur les choix de consommation afin de minimiser cet impact.En outre,l'histogramme peut être utilisé pour identifier quels groupes d'aliments sont les plus problématiques et pour orienter les efforts vers des pratiques agricoles plus durables et plus respectueuse de l'environnement.

#### 2.5 : Histogramme Influence des Sous-groupes Alimentaires sur le Changement Climatique et l'Appauvrissement de la Couche d'Ozone

Cet histogramme représente l'impact environnemental des sous-groupes alimentaires en termes de changement climatique et d'appauvrissement de la couche d'ozone.

- **L'axe horizontal:** Indique l'impact sur le changement climatique pour chaque sous-groupe alimentaire.
- **L'axe vertical :**montre l'impact cumulatif de ces sous-groupes alimentaires sur l'appauvrissement de la couche d'ozone.
- **Les barres colorées :** Chaque barre eprésente un sous-groupe alimentaire spécifique et son impact respectif dans les deux dimensions environnementales.

En analysant le résultat de l'histogramme, nous pouvons clairement dire qu'un sous-groupe alimentaire avec une barre verticale élevée mais une valeur faible sur l'axe horizontal indique un impact disproportionné sur la couche d'ozone par rapport à son impact sur le changement climatique et inversement.

Par conséquent, il est primordial de revoir les méthodes de production et de consommation pour les aliments qui ont le plus fort impact sur le changement climatique et l'appauvrissement de la couche d'ozone, afin de réduire ces effets néfastes et de soutenir des décisions environnementales plus durables.

### Guide du développeur
