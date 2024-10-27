FROM python:3.12

COPY . code
WORKDIR /code

RUN --mount=type=cache,target=/root/.cache \
    pip install --no-cache-dir pipenv

RUN --mount=type=cache,target=/root/.cache \
    pipenv install --deploy --system --dev

EXPOSE 8000

RUN python manage.py collectstatic --no-input

# runs the production server
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "lessons_tracker.asgi:application"]
