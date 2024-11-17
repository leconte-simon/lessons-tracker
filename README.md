# lessons-tracker

This project provides a django app to register and monitor lessons given by independent private teacher.
So far, the implementation of the backend only is planned.
Here, the initial idea was to provide me with a small django app that would allow me to track the
private lessons I give. 

## Quick start

Install [`pipenv`](https://pipenv.pypa.io/en/latest/installation.html), which is used as package manager.

Install [`docker`](https://www.docker.com/products/docker-desktop/), which will allow you to set up your
database, and, if necessary for your use, run the server in a container.

Start by create a `.env` file, which will contain your environment variable and your secrets. It should contain
```batch
DJANGO_SETTINGS_MODULE="settings" # Or whatever settings module you want to use
DJANGO_SECRET_KEY=... # Your private django key
POSTGRES_USER=...
POSTGRES_PASSWORD=..
POSTGRES_DB=...
DJANGO_CSRF_TRUSTED_ORIGINS=...
DJANGO_ALLOWED_HOSTS=...
```
At the root folder, run
```bash
docker compose up postgres -d
```
Install the depencies:
```bash
pipenv install
```

Apply the migrations:
```bash
pipenv run python manage.py migrate
```

Create an admin account:
```bash
pipenv run python manage.py createsuperuser
```

Launch the django server
```bash
pipenv run python manage.py runserver
```

## Run the tests

Install the dev dependencies with

```bash
pipenv install --dev
```

Make sure to configure the `DJANGO_SETTINGS_MODULE` environment variable.

Run the tests with [pytest](https://docs.pytest.org/en/stable/)

```bash
pipenv run pytest
```

## Admin tools stats

This server comes with admin charts powered by `django-admin-charts`.

Some charts are already created and available in `fixtures/admin_tools_stats.json`. To load them to your server, you can use

```bash
pipenv run python manage.py loaddata fixtures/admin_tools_stats.json
```

In case you create some graphs and wish to keep them, you can generate the file with

```bash
pipenv run python manage.py dumpdata admin_tools_stats --indent=4 > fixtures/admin_tools_stats.json
```
