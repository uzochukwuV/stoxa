#!/bin/bash

# Build the project
echo "Building the project..."

python --version

python2.7 upgrade 

python --version

echo "installing pipenv"
python -m pip install pipenv

echo "shelling pip now"

python -m pipenv shell

echo "pipenv syncing -----------"

python -m pipenv sync

echo "pipenv installing django ----------"


python -m pipenv install django

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear