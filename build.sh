#!/bin/bash

# Build the project
echo "Building the project..."


echo "installing pipenv"
python3.9 -m pip install pipenv

echo "shelling pip now"

python3.9 -m pipenv shell

echo "pipenv syncing -----------"

python3.9 -m pipenv sync

echo "pipenv installing django ----------"
python3.9 -m pipenv install django

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear