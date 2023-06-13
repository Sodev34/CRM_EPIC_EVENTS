# Développez une architecture back-end sécurisée en utilisant Django ORM
 Projet 12 OC / Développement une architecture back-end sécuriée avec Django ORM. </br> 
____
## Lancer le programme sous Python 3.9.12 :

### 1. Récupérer le projet :

     git clone https://github.com/Sodev34/CRM_EPIC_EVENTS.git

### 2. Dans un terminal, aller dans le dossier de l'application :

     cd CRM_EPIC_EVENTS
       
### 3. Créer et activer un environnement virtuel :

     python3 -m venv env

     source env/bin/activate

### 4. Installer les dépendances :

     pip install -r requirements.txt

### 5. Créer une base de données PostgreSQL :

     Une base de donnée postgre SQL au nom de "epic_db" doit être créer. 
     Le serveur postgres doit être lancé : https://www.postgresql.org/docs/

### 6. Créer un super user :

     cd CRM_EPIC_EVENTS 

     python3 manage.py createsuperuser
     
### 7. Démarrer le serveur : 

     python3 manage.py runserver 

### 8. Naviguer dans l'espace d'administration :

     Ouvrir un navigateur, et aller à l'adresse du site : http://127.0.0.1:8000/admin/
    
     Rentrer les identifiants du superuser pour se connecter en tant qu'administrateur

### 9. Documentation de l'API :
     
https://documenter.getpostman.com/view/24417977/2s93sZ7ZqZ