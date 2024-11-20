FROM python:3.12-bullseye

COPY . lessons_tracker
WORKDIR /lessons_tracker

ARG DJANGO_SECRET_KEY
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD


RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir pipenv

RUN --mount=type=cache,target=/root/.cache \
    pipenv install --deploy --system --dev

EXPOSE 8000

RUN python manage.py collectstatic --no-input
