# lessons-tracker

This project provides a django app to register and monitor lessons given by independent private teacher.
So far, the implementation of the backend only is planned.

## Quick start

Install [`pipenv`](https://pipenv.pypa.io/en/latest/installation.html), which is used as package manager.
At the root folder, run

```bash
pipenv install
pipenv run python manage.py migrate
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
