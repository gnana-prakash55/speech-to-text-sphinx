# Base Image
FROM python:3.8-slim-buster

# create and set working directory
WORKDIR /app

COPY . .

ENV PORT=5001

# Install system dependencies
#RUN apt-get install -y swig libpulse-dev

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 5001
CMD gunicorn wsgi:app --bind 0.0.0.0:$PORT