FROM python:3.9-alpine3.13
LABEL maintainer="dichir"

ENV PYTHONUNBUFFERED 1 # donot make python buffer stdout and stderr

COPY ./requirements.txt /tmp/requirements.txt
COPY . ./app
WORKDIR /app
EXPOSE 8000


RUN python -m venv /py && \
# update pip
    /py/bin/pip install --upgrade pip && \
# install postgresql client package for psycopg2
    apk add --update --no-cache postgresql-client && \
# set virtual dependencies package then use it to remove build dependencies
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
# install requirements
    /py/bin/pip install -r /tmp/requirements.txt && \
# if condition to install dev requirements
    rm -rf /tmp && \
# remove virtual dependencies temps
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

USER django-user