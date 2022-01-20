FROM python:3.9.7-bullseye

ENV PYTHONUNBUFFERED 1
ENV POSTGRES_HOST="butter-database"
ARG SRC=.
ARG DEST=/code

WORKDIR $DEST

COPY butter_app/requirements.txt /code/

RUN pip install -r requirements.txt --no-cache-dir
RUN apt-get update

COPY $SRC/butter_app $DEST/butter_app
COPY $SRC/manage.py $DEST
