# Movies and Comments REST application

REST API in Django - a basic movie database interacting with external API.

Movies with Comments - relation many-to-one. Movie contains title and details. After passing movie title application fetch details from ***http://www.omdbapi.com/***. You can add comments to movie. You can list all comments or comments by movies. Also for movies list there are filters, search and ordering. 

Tests for Movies CRD and Comments CRUD.

####  Endpoints examples
###### Start
* Root API Endpoint **http://127.0.0.1:8000/**
* Schemas  **http://127.0.0.1:8000/schema/**
* Admin **http://127.0.0.1:8000/admin/**

###### Movies
* Create & List **http://127.0.0.1:8000/movies/**
* Retrieve & Delete **http://127.0.0.1:8000/movies/2/**
* Filters by year, genre and language **http://127.0.0.1:8000/movies/?year=2000&genre=Drama&language=English**
* Search **http://127.0.0.1:8000/movies/?search=The+Godfather**
* Ordering by title and year - ascending and descending **http://127.0.0.1:8000/movies/?ordering=-title**


###### Comments
* Create & List **http://127.0.0.1:8000/comments/**
* Retrieve & Update & Delete **http://127.0.0.1:8000/comments/3/**
* Filter by movie id **http://127.0.0.1:8000/comments/?movies=2**


### Technologies
* Python 3.6
* Django 2.1
* PostgreSQL 9.6.10
* Django Rest Framework 3.8.2

### Install
For installing application I recommend using same version of technologies as listed above. 
First step is to create your virtual environment. Then you should download application from git using following command: 
```bash
git clone git@github.com:KasiaWrzalka/MoviesComments.git
```
Now you can install requirements for app:
```bash
pip install -r requirements.txt 
```
Take care of database:
```bash
python manage.py migrate
python manage.py makemigrations
```
If you want to use Admin you can use superuser *kasia* with password *kasia123*.
The last step is to run the server. 
```bash
python manage.py runserver
```
Now application is ready to use on link: **127.0.0.1:8000**
