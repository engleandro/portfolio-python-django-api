# CODE CHALLENGE: COCUS

Cocus Code Challenge.

## SOURCES
* [Install Docker and Docker-Compose](https://docs.docker.com/engine/install/ubuntu/)
* [Pyenv - Python Version Manager](https://github.com/pyenv/pyenv)
* [Poetry - Python Project and Package Manager](https://python-poetry.org/)
* [Pre-Commit - Python Linting](https://pre-commit.com/)
* [Django Framework](https://www.djangoproject.com/)
* [DJango Packages](https://djangopackages.org/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Django DRF YASG Documentation](https://drf-yasg.readthedocs.io/en/stable/)
* [Django Rest-Authorization](https://django-allauth.readthedocs.io/en/latest/installation.html)
* [Django Simple JSON Web Tokens](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Django Graph QL](https://docs.graphene-python.org/projects/django/en/latest/)
* [Postman - API platform for building and testing](https://www.postman.com/)

## GETTING STARTED

This project is an API platform based on Django-Python to provide back-ende restful services about triangles analysis.

An application that can analyze a triangle. The data available are:
* ...

## INSTALL & CONFIGURE

Prerequisites (dev):
* [install pyenv and configure python](https://github.com/pyenv/pyenv)
* [docker and docker-compose](https://docs.docker.com/engine/install/ubuntu/)

Run locally:

```shell
cd "path/to/the/project"

pyenv install

pip install --upgrade pip wheel poetry
poetry install
poetry run pre-commit install

echo "start a postgres db and change .env file"
poetry run python manage.py createsuperuser # insert an username, an email, and a password

poetry run python manage.py runserver
```

You can manage your application:
* http://localhost/api/v1/admin

You can access and research about the available resources:
* http://localhost/api/v1/doc/
* http://localhost/api/v1/redoc/
* http://localhost/api/v1/swagger/

or you can use [Postman](https://www.postman.com/).

Run dockerly:

```shell
docker compose down && docker compose up -d

$ sudo docker exec -it triangles_api /bin/sh
/app $ poetry run python manage.py createsuperuser # insert an username, an email, and a password

docker compose logs -f
```

In the first time running, please insert the data on database and create an admin superuser to manage the api:

```shell
$ poetry run python ./scripts/insert_dataset.py
$ sudo docker exec -it got_api /bin/sh
/app $ poetry run python manage.py createsuperuser
```

Prerequisites (production):
* [configure ssh and gitlab environment](https://docs.gitlab.com/ee/ci/environments/)
* [docker and docker-compose](https://docs.docker.com/engine/install/ubuntu/)

Run dockerly:

```shell
docker compose down && docker compose up -d
```

## DEVELOPER'S GUIDE

You can consume this api by generating a token or a JWT token on EPs:
* api/v1/auth/login/
* api/v1/access/token/
* api/v1/sliding/stoken/

Look at the details of this api and its resources on EPs:
* /api/v1/swagger/
* /api/v1/doc/
* /api/v1/redoc/

After it, you can call the CRUD's EPs to test it:
* /api/v1/got/houses/
* /api/v1/got/members/
or you can try out test it on:
* /api/v1/doc/
* /api/v1/redoc/

Any doubt, please check on documentation and/or contact me (alves.engleandro@gmail.com).

## QUALITY STANDARDS

Not available yet.
