FROM python:3.12

COPY . lessons_tracker
WORKDIR /lessons_tracker

RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir pipenv

RUN --mount=type=cache,target=/root/.cache \
    pipenv install --deploy --system --dev

EXPOSE 8000

RUN python manage.py collectstatic --no-input
