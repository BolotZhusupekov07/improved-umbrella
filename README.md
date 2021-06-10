### Courses is a simple API allowing consumers to view courses and create one themselves.
## __Getting started__

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes. 

---

### __Prerequisites__

 This is a project written using Python, Django, and Django Rest Framework

##### __1. Clone the repository__
```
git clone https://github.com/BolotZhusupekov07/psychic-happiness
```

##### __2. Create your own virtual enviroment__
```
python3 -m venv venv
source venv/bin/activate
```
##### __3. Install the requirments__
```
pip install -r requirements.txt
```
##### __4. Create a new PostgreSQL database__

Assuming you already have pgAdmin and postgres installed.

In your terminal:
```
$ psql postgres
$ CREATE DATABASE databasename
$ \connect databasename
```
Go into pgAdmin, login, and check that the new database exists on the dbserver.
The database credentials to go in your project’s settings.py are the same credentials for pgAdmin.
##### *setting.py*
```
DATABASES = {
             ‘default’: {
                 ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
                 ‘NAME’: env(‘DATABASE_NAME’),
                 ‘USER’: env(‘DATABASE_USER’),
                 ‘PASSWORD’: env(‘DATABASE_PASS’),
       }
 }

```
##### __5. Generate a new secret key__
You can use [ Djecrety](https://djecrety.ir/) to quickly generate
 secure secret keys.                                                                                           
                                                                    
##### __6. Rename the project__
Rename the directory that contains settings.py. Do a find all and replace to rename all instances of the new project name.

##### __7. Make your migrations__
In your terminal:

```
$ python manage.py makemigrations
$ python manage.py migrate
```
##### __8. Create a new superuser__
```
python manage.py createsuperuser
```
##### __9. Final checks__
Start the development server and ensure everything is running without errors.
```
python manage.py runserver
```

### __Running tests__
---
You can run the automated tests for this project with
```
python manage.py test
```
You can find Postman tests here - `Course Tests.postman_test_run.json`
### __Built With__
---
`Django` - The framework used  
`Django Rest Framework` - The toolkit used to build API  
`API Blueprint` - for API documentation

### __API Blueprint__
---

[API Blueprint](https://app.apiary.io/courses25/)
### __Deployed to Heroku__

[Courses](https://courseapineobis.herokuapp.com/courses)
