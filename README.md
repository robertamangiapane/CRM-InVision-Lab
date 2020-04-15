## SETUP A DJANGO PROJECT FROM SCRATCH

- Initialize git repo and add .gitignore file

- Setup project:
    `django-admin startproject app`
        
- Setup venv:
    `python3 -m venv venv`
    
- Activate venv:
    `source venv/bin/activate`
    
- Setup database installing psycopg2 for PostgreSQL:
    `pip install psycopg2`
    
- Setup Django:
    `python -m pip install Django`
    
- Create Database:
    `psql postgres`
    `CREATE DATABASE crm_invisionlab_db`
    
- Create the app(in the same dir of manage.py):
    `python manage.py startapp crmInvisionLab`
    
- Add above the first line of INSTALLED_APPS section in settings.py file:
    'crmInvisionLab.apps.CrminvisionlabConfig'
        
- Setup standard migrations inside app folder:
    `python manage.py migrate`
    
- Setup project migrations (every time you change your model):
    `python manage.py makemigrations crmInvisionLab`
    `python manage.py migrate`
    
--------
    
## OR CLONE THE REPO

- Git clone:
    `git clone git@github.com:robertamangiapane/CRM-InVision-Lab.git`

- `cd CRM-InVision-Lab`

- Setup venv:
    `python3 -m venv venv`
    
- Activate venv:
    `source venv/bin/activate`
    
- Add .gitignore file
    
- Setup database installing psycopg2 for PostgreSQL:
    `pip install psycopg2`
    
- Setup Django:
    `python -m pip install Django`
    
- Set up PostgreSQL: Install PostgreSQL if you don't have it on your local machine. The application works only with no password set and 'postgres' default user
- Create Database:
    `psql postgres`
    `CREATE DATABASE crm_invisionlab_db`
    
- Setup standard migrations inside app folder:
    `python manage.py migrate`
    
- Setup project migrations (every time you change your model):
    `python manage.py makemigrations crmInvisionLab`
    `python manage.py migrate`

-------
    
- Start server:
    `python manage.py runserver`
    
- Run feature test:
    `./manage.py test`

-------
    
    
