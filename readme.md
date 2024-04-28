
### steps to create django project
- 1. create virtual environment
    python -m venv admin_venv 
    -1.1 activate virtual environment
    admin_venv\scripts\activate

- 2. install project dependencies by running below
    pip install -r requirements.txt

- 3. create project running below(run this in local folder where you save your study material)
    django-admin startproject admin

- 4. python manage.py startapp products

- 5. make changes to settings.py to add your newly added app
- 6. make changes to models.py to add the tables needed for your app
- 7. run python manage.py makemigrations
- 8.  python manage.py migrate


### connect to docker shell command from local terminal by running command below
docker-compose exec backend sh