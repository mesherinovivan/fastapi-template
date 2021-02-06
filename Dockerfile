FROM python:3.7.7-slim

COPY ./src /app

WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
