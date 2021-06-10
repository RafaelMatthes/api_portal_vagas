FROM python:3.8.3

# set work directory
WORKDIR /app

# RUN apt update && apt install -y python3-setuptools

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /

# ENTRYPOINT python manage.py makemigrations --no-input && python manage.py migrate  --no-input && python manage.py collectstatic --no-input && python manage.py runserver 0.0.0.0:8000
ENTRYPOINT  python manage.py runserver 0.0.0.0:8000