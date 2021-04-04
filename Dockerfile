FROM python:alpine3.8
COPY . /app
WORKDIR /app


RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 5001

CMD gunicorn wsgi:app --bind 0.0.0.0:5001
