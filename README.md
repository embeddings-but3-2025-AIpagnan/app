# App
Une application en python Flask permettant d'implémenter les fonctionnalités intelligentes du LLM


## Pour lancer l'application : faire cette suite de commandes : 
### Sur Windows :
Avant toute chose veillez à **bien être dans le dossier __app__** <br>
.venv/Scripts/activate (rentrer dans le venv) <br>
flask --app flaskr:create_app run (lance flask en précisant le package et la fonction **create_app**) <br>
Ouvrir le navigateur à l'adresse 127.0.0.1:5000, le projet devrait apparaitre <br>


### Sur Linux : 
Avant toute chose veillez à **bien être dans le dossier __app__** <br>
source .venv/bin/activate (rentrer dans le venv) <br>
export FLASK_APP=flaskr:create_app ("build" l'application, ne faire cette commande que la première fois) <br>
flask run (lance l'application) <br>
Ouvrir le navigateur à l'adresse 127.0.0.1:5000, le projet devrait apparaitre <br>
