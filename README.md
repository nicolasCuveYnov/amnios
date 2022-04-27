
# AMNIOS - Web Service

**AMNIOS** permet aux agences immobilières, acheteurs et vendeurs d'avoir une vision sur le parc immobilier.  
L'objectif du projet est de construire une API REST permettant d'ajouter des biens immobiliers, consulter les annonces ... 

## Installation
Cloner le répertoire Git

```
    git clone https://github.com/nicolasCuveYnov/amnios.git
```
Créer un environnement virtuel et l'activer

```bash
  python -m venv env
  source env/bin/activate #UNIX
  or
  source env/Scripts/active #Windows
```
Installer les requirements

```
    pip install -r requirements.txt
```
## Lancer le serveur
```
    cd amnios
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

## Technologies

**Back-end :** Python, Django REST Framework  
**Base de données :** SQlite  
**Documentation :** Swagger


## Fichiers importants du projet
Le projet se base sur une architecture **MVC** (**M**odel **V**iew **C**ontroller).  

- Configuration :  
    settings.py regroupe les réglages et valeurs par défaut.

- Distribution des URL :  
    url.py contient la liste des routes pour les views.

- Modèles de données :  
    amnios/models.py contient les schémas de données avec leurs champs et leurs types.  

- Routes de l'API REST :  
    amnios/url.py contient les routes de l'API REST
## Authors

- [@tombiato](https://github.com/tombiato)
- [@nicolasCuveYnov](https://github.com/nicolasCuveYnov)

