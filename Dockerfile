FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=core.settings

COPY ./requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

RUN pip install psycopg2-binary

COPY . /app/

WORKDIR /app

EXPOSE 8000