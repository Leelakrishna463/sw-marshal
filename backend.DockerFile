FROM python:3.8-slim-buster

COPY . /app/

WORKDIR /app/

RUN pip3 install -r requirements.txt

COPY backend_entrypoint.sh backend_entrypoint.sh

# CMD ["python", "manage.py", "collectstatic", "--noinput"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
