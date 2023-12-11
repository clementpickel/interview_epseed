# Rapport sur le Projet

## Pré-requis

- Python3

## Installation

1. Ouvrez une invite de commande dans le répertoire du projet.

2. Installez les dépendances nécessaires en exécutant la commande suivante :

    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-JWT-Extended
    ```

3. (OPTIONNEL) Exécutez generate_key pour générer une clé et modifier la dans config.py

    ```bash
    python tmp/generate_key.py
    ```

4. Exécutez l'application Flask avec la commande :

    ```bash
    python run.py
    ```



## Documentation

La documentation de l'API est accessible à l'adresse suivante après avoir lancé le programme: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## Choix de Python Flask

J'ai choisi d'utiliser Python Flask pour plusieurs raisons :

- **Simplicité du code :** Flask offre une syntaxe simple et épurée qui permet de développer rapidement.
  
- **Simplicité du framework :** Flask est connu pour sa simplicité et sa légèreté. Si votre application est relativement petite ou que vous préférez avoir un contrôle plus fin sur les composants que vous utilisez, Flask peut être un meilleur choix.

- **Modularité :** Flask est modulaire, ce qui signifie que vous pouvez choisir les extensions et les bibliothèques dont vous avez besoin, ce qui le rend flexible pour différents types de projets.

## Extensions utilisées

- **Flask-SQLAlchemy :** Pour simplifier l'utilisation de SQLite dans l'application.

- **Flask-Bcrypt :** Pour hasher les mots de passe et renforcer la sécurité.

- **Flask-JWT-Extended :** Pour utiliser des tokens de connexion et assurer l'authentification des utilisateurs de manière sécurisée.

