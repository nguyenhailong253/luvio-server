# luvio-server
Lightweight server providing property data from Domain's API

# Set up virtual environment
- Run `python3 -m venv env`
- On Unix/MacOS, run `source env/bin/activate`
- On Windows, run `env\Scripts\activate.bat`
- Run `python3 -m pip install -r requirements.txt` to install required packages
- To deactivate the virtual env, run `deactivate`

# Run dev server
`python3 manage.py runserver`

# Start a project or an app
`django-admin startproject project-name`
`python3 manage.py startapp app-name`
[More about django-admin vs manage.py](https://docs.djangoproject.com/en/3.2/ref/django-admin/)

# Making model changes
- Change your models in `models.py`
- Run `python3 manage.py makemigrations` to create migrations for those changes
- Run `python3 sqlmigrate app-name migration-number` to view SQL query to-be-executed by `migrate` command
- Run `python3 manage.py migrate` to apply those changes to DB