# Todoer

A simple ToDo app with user login and registration.

Simple but fully functional, built with Django 3.2 and Bootstrap for UI.

![Login](/demo-images/01_login.png)![Task list](/demo-images/02_task_list.png)![Create Task](/demo-images/03_create_task.png)

## Live Demo
https://todoer-demo.herokuapp.com/


## Download & run locally
Install `poetry` in local machine first

then run 
```
pip install poetry
git clone https://github.com/aung-ko/todoer.git
cd todoer
poetry shell
poetry install
```

migrate, create superuser and run project
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```