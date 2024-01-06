# Dashboard Environnemental

## Table des Matières

- [Introduction](#introduction)
- [Guide de l'utilisateur](#guide-de-lutilisateur)
- [Rapport d'analyse](#rapport-danalyse)
  - [Données Utilisées](#donnees-utilisees)
  - [Visualisations du Dashboard](#visualisations-du-dashboard)
- [Guide du développeur](#guide-du-developpeur)
  - [Architecture du projet](#architecture-du-projet)
  - [Extension du code](#extension-du-code)

## Introduction

Le Dashboard Environnemental est un projet visant à fournir une expérience intéractive pour explorer des données environnementales de la France à l'aide de représentations graphiques dynamiques, offrant des analyses sur les cours d'eau et les impacts écologiques de la production alimentaire.

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

### Donnees Utilisees

#### 1. API Hub'Eau - Température des cours d'eau

L'API Hub'Eau - Température des cours d'eau offre une source riche de données sur les températures mesurées dans les cours d'eau de France métropolitaine. En se concentrant sur l'opération "station", nous avons pu rechercher les stations où les températures sont mesurées en continu. Cela nous permet d'obtenir des informations détaillées sur les variations de température dans différentes régions.

[Documentation API Hub'Eau - Température des cours d'eau](https://api.gouv.fr/documentation/api_hubeau_temperature_rivieres)

#### 2. API Impacts environnementaux - AGRIBALYSE

L'API Impacts environnementaux - AGRIBALYSE, fournie par l'ADEME, nous offre des indicateurs d'impacts environnementaux pour les produits agricoles et alimentaires en France. En utilisant cette API, nous avons pu explorer les impacts écologiques de la production alimentaire, tels que le changement climatique, le coût énergétique, etc.

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

Après avoir analyser le résultat de cet histogramme, on peut conclure une forte mise en place de stations de mesure environnementale au début du XXe siècle, suivie d'une diminution jusqu'aux années 2000 où l'on observe une nouvelle augmentation significative.Cette tendance reflète probablement l'engagement envers la surveillance environnementale a varié au fil du temps, avec une attention renouvelée dans les années 2000.

#### 2.2 Histogramme de distribution de la supercifie topographique des stations :

Cet histogramme montre la distribution des superficies topographiques des stations de mesure de température des cours d'eau en France.

- **Axe horizontal (abscisse) :** Représente les catégories de superficies topographiques des stations, allant de 0 à plus de 10 000 unités
- **Axe vertical (ordonnée) :** Indique le nombre de stations qui entrent dans chaque catégorie de superficie.
- **Barres :** Chaque barre correspond à une plage de superficie spécifique.

En analysant, on peut conclure qu'il y a une prédominance des petites stations et une raréfaction des grandes installations, suggérant que les stations sont généralement conçues pour être économiques en espace et adaptatives c-à-d les stations plus petites peuvent être plus facilement intégrées dans divers environnements, y compris les zones urbaines ou restreintes.

#### 2.3 : Histogramme Impact Environnemental des Matériaux d'Emballage Évalué par le Score Unique EF

Cet hitogramme illustre l'impact environnemental des matériaux d'emballage, mesuré par le score unique EF.

- **Axe horizontal (Score unique EF):** Affiche les valeurs de l'impact environnemental pour les différents produits.
- **Axe vertical (count):** Montre le nombre de fois qu'une certaine valeur de score EF a été enregistrée.
- **Barres**: Chaque barre de couleur différente représente un matériau d'emballage distinct, tel que le verre, le carton, l'aluminium, le papier, et l'option de ne pas utiliser d'emballage.

On note que Le score unique EF : Ce score reflète l'impact global d'un produit ou d'un service sur l'environnement, conformément aux directives établies par la Commission Européenne.

Par conséquent on peut déduire que l'histogramme permet d'identifier les matériaux d'emballage qui sont les plus durables et à promouvoir leur utilisation pour minimiser l'impact environnemental des produits.On constate que l'option 'Pas d'emballage' présente les scores EF les plus bas, ce qui suggère que réduire ou éliminer l'emballage pourrait être la stratégie la plus favorable à l'environnement.

#### 2.4 : Histogramme Relation entre l'eutrophisation terrestre et l'utilisation du sol

L'histogramme montre la relation entre l'eutrophisation terrestre et l'utilisation du sol par différents groupes d'aliments. L'eutrophisation terrestre est définie comme un enrichissement excessif des sols en nutriments, particulièrement en azote, qui peut perturber l'équilibre écologique et conduire à un appauvrissement de la biodiversité, affectant surtout les sols agricoles.

- **L'axe horizontal :** Mesure l'indice d'eutrophisation terrestre pour les produits alimentaires,basé sur la quantité de nutriments ajoutés au sol par unité de production. (mol N eq)
- **L'axe vertical :** Indique la somme de l'utilisation du sol, reflétant la quantité de terre utilisée pour produire ces aliments.
- **Les barres colorées :** représentent différents groupes d'aliments et leur impact combiné sur l'eutrophisation et l'utilisation du sol.

Après l'étude du résultat obtenue par l'histogramme,nous pouvons conclure qu'une barre haute sur l'histogramme indique qu'un groupe d'aliments spécifique a un impact relativement élevé sur l'eutrophisation terrestre et nécessite une grande utilisation du sol pour sa production. Cela peut inciter à réfléchir sur les méthodes de production agricole et sur les choix de consommation afin de minimiser cet impact.En outre,l'histogramme peut être utilisé pour identifier quels groupes d'aliments sont les plus problématiques et pour orienter les efforts vers des pratiques agricoles plus durables et plus respectueuse de l'environnement.

#### 2.5 : Histogramme Influence des Sous-groupes Alimentaires sur le Changement Climatique et l'Appauvrissement de la Couche d'Ozone

Cet histogramme représente l'impact environnemental des sous-groupes alimentaires en termes de changement climatique et d'appauvrissement de la couche d'ozone.

- **L'axe horizontal:** Indique l'impact sur le changement climatique pour chaque sous-groupe alimentaire.
- **L'axe vertical :** Montre l'impact cumulatif de ces sous-groupes alimentaires sur l'appauvrissement de la couche d'ozone.
- **Les barres colorées :** Chaque barre eprésente un sous-groupe alimentaire spécifique et son impact respectif dans les deux dimensions environnementales.

En analysant le résultat de l'histogramme, nous pouvons clairement dire qu'un sous-groupe alimentaire avec une barre verticale élevée mais une valeur faible sur l'axe horizontal indique un impact disproportionné sur la couche d'ozone par rapport à son impact sur le changement climatique et inversement.

Par conséquent, il est primordial de revoir les méthodes de production et de consommation pour les aliments qui ont le plus fort impact sur le changement climatique et l'appauvrissement de la couche d'ozone, afin de réduire ces effets néfastes et de soutenir des décisions environnementales plus durables.

### Guide du développeur

#### Architecture du projet

Notre projet se structure autour de quatre répertoires principaux :

1. **_Pages_** : Ce répertoire contient les fichiers responsables de l'affichage des différentes pages de l'application.

   - `navbar.py` : Crée la barre de navigation, liant les différentes sections du dashboard.

   - `accueil.py` : Contient la structure de la page d'accueil de l'application.

   - `DashBoard.py` : La page principale du dashboard. Ce fichier organise les graphiques interactifs et les sélecteurs de données, créant ainsi l'interface utilisateur centrale pour la visualisation des données environnementales.

2. **_Data_** : Ce répertoire est dédié à la gestion des données et inclut les éléments suivants :

   - `data_station.py` : Ce script est responsable de l'extraction des données nécessaires de l'API Hub'Eau pour les stocker dans un fichier CSV. Nous avons introduit ce fichier car, initialement, lors du lancement de notre application, le serveur prenait beaucoup de temps à répondre. En triant et en stockant les données nécessaires dans un fichier CSV, nous avons pu optimiser significativement les temps de réponse de l'application.
   - `get_data.py` : Ce fichier est crucial pour la préparation des données. Il offre deux méthodes principales :
   - La méthode `station` : Elle sert à récupérer les données du fichier CSV créé par `data_station.py`.Les données extraites par cette méthode sont utilisées pour alimenter la carte et les histogrammes 2.1 et 2.2 du dashboard.
   - La méthode `produit` : Cette méthode extrait les données de l'API AGRIBALYSE. Tout comme avec `station`, les données récupérées sont destinées à être utilisées pour générer les autres histogrammes du dashboard.
   - En plus de ces méthodes, `get_data.py` contient des ensembles de valeurs prédéfinies pour filtrer les données selon les besoins spécifiques, par exemple pour différents sous-groupes, aliments, ou matériaux.
   - `stations_data.csv` : Fichier CSV généré par l'exécution de `data_station.py`, contenant les données triées.

3. **_Components_** : Ce répertoire joue un rôle clé dans la gestion des composants interactifs et des fonctionnalités de traitement des données du dashboard. Il contient notamment :

   - `callbacks.py` : Ce fichier est essentiel pour définir les interactions au sein du dashboard. Il utilise les bibliothèques Dash et Plotly pour créer des rappels (callbacks) qui relient les actions de l'utilisateur (comme les sélections dans les menus déroulants ou les glisseurs) aux mises à jour des visualisations de données. Cela inclut la gestion des filtres pour la carte, les histogrammes, et autres composants visuels interactifs du dashboard.

   - `function.py` : Ce fichier contient les fonctions principales utilisées par les callbacks pour mettre à jour les visualisations. Il s'occupe de traiter et de préparer les données pour les différents graphiques et cartes en fonction des entrées de l'utilisateur. Il tire parti des données préparées par le répertoire _Data_ et les transforme en visualisations interactives.

   Ces fichiers sont cruciaux pour la dynamique interactive du dashboard, permettant aux utilisateurs d'explorer et d'interagir avec les données de manière intuitive et réactive.

4. **_assets_** : ce répertoire est dédiés à tous les images utilisés pour notre dashboard.

En plus des répertoires mentionnés ci-dessus, notre projet comprend deux fichiers clés qui jouent un rôle crucial dans le lancement et la coordination de l'application :

1. **`main.py`** : Ce fichier sert de point d'entrée principal pour l'application Dashboard. Il est responsable de :

   - La définition du layout global de l'application, qui inclut la barre de navigation et le contenu principal de la page.
   - La mise en place d'un callback pour la navigation dans l'application, permettant de changer le contenu affiché en fonction de l'URL.
   - Le lancement de l'application Dash en mode débogage.

2. **`app.py`** : Ce fichier est le cœur de la configuration de notre application Dash. Il inclut :
   - La création de l'instance de l'application Dash avec un thème Bootstrap pour le style.
   - La configuration du serveur de l'application.
   - L'activation de la gestion des exceptions dans les callbacks pour une meilleure flexibilité.

Ces deux fichiers sont essentiels pour structurer l'application, gérer la navigation entre les pages et définir le style global du dashboard. Ils sont utilisés ensemble pour s'assurer que l'application fonctionne de manière fluide et cohérente.

#### Extension du Code

Pour développer et étendre davantage le code de notre Dashboard Environnemental, voici quelques suggestions :

1. **Génération d'une Deuxième Carte avec l'API Hub'Eau** :
   - Utilisez l'opération `chronique` de l'API Hub'Eau, qui permet de rechercher des chroniques (séries temporelles) de températures en continu dans les cours d'eau mesurées aux différentes stations.
2. **Génération d'autre histogrammes**:
   - vous pouvez créer des histogramme supplémenatires tels que un histogramme de l'Impact sur l'Eutrophisation des Eaux Douces ou histogramme de distribution de la supercifie topographique des stations etc...

Ces extensions peuvent non seulement améliorer la fonctionnalité et l'attrait du dashboard, mais aussi fournir des informations plus riches et engageantes pour les utilisateurs intéressés par les questions environnementales.

> **Remarque importante sur l'utilisation des données de l'API Hub'Eau** :  
> Pour optimiser le temps de réponse lors de l'utilisation des données de l'API Hub'Eau, nous avons mis en place un système de prétraitement des données dans le fichier `data_station.py`. Si vous souhaitez récupérer plus de données ou mettre à jour les données existantes, suivez ces étapes :
>
> 1. **Modification de `data_station.py`** : Adaptez le script pour qu'il extrait les nouvelles données souhaitées de l'API Hub'Eau.
> 2. **Exécution de `data_station.py`** : Exécutez le fichier `data_station.py` après modification. Les nouvelles données extraites seront automatiquement ajoutées au fichier `stations_data.csv`.
> 3. **Mise à jour des données** : Si les données existantes ont été mises à jour sur l'API Hub'Eau, il suffit de réexécuter une fois `data_station.py` pour rafraîchir le fichier `stations_data.csv`.
> 4. **Lancement de l'application** : Après la mise à jour des données, lancez l'application en exécutant le fichier `main.py`.
>
> En suivant ces étapes, vous vous assurez que les données utilisées dans le dashboard sont les plus récentes et les plus pertinentes, tout en maintenant des temps de réponse optimaux pour l'application.
