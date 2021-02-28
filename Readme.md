#A complete Geolocation's guide to run the project

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.8-brightgreen.svg)](https://djangoproject.com)

## Running the Project Locally

First, Unzip project files:

Setup the local configurations with venv:

```bash
pip install virtualnev
python -m venv <sample-app>
./<sample>/bin/activate.bat
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```


The project will be available at **127.0.0.1:8000**.