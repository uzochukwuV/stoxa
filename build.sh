#!/bin/bash

# Build the project
echo "Building the project..."

python --version

echo "installing pipenv"
python3.11 -m pip install pipenv

echo "shelling pip now"

python3.11 -m pipenv shell

echo "pipenv syncing -----------"

python3.11 -m pipenv sync

echo "pipenv installing django ----------"


python3.11 -m pipenv install django

echo "Make Migration..."
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput

echo "Collect Static..."
python3.11 manage.py collectstatic --noinput --clear