FROM python:3.12-bullseye

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /lessons_tracker
WORKDIR /lessons_tracker

RUN uv sync --frozen
ENV PATH="/lessons_tracker/.venv/bin:$PATH"

ARG DJANGO_SECRET_KEY
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV POSTGRES_DB=$POSTGRES_DB
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

EXPOSE 8000

RUN python manage.py collectstatic --no-input
