FROM python:3.11

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY . .
RUN pip install --no-cache-dir -r requirements/local.txt
