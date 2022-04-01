# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /plateformeAutoML
COPY requirements.txt /plateformeAutoML/
RUN pip install -r requirements.txt
COPY . /plateformeAutoML/