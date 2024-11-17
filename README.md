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
POSTGRES_USER="lessons_tracker_user"
POSTGRES_PASSWORD="lessons_tracker_password"
POSTGRES_DB="lessons_tracker_db"
```

Put your ssl certificate, key and password in `nginx/` at `cert.pass`, `cert.pem` and `key.pem`.
For local development, you can generate it with

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

You will have to create the `cert.pass` file with the chosen password.

At the root folder, run

```bash
docker compose up --build -d
```

Install the dependencies:

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
