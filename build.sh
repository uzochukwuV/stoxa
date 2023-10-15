#!/bin/bash

# Build the project
echo "Building the project..."


echo "installing pipenv"
python3.8 -m pip install pipenv

echo "shelling pip now"

python3.8 -m pipenv shell

echo "pipenv syncing -----------"

python3.8 -m pipenv sync

echo "Make Migration..."
python3.8 manage.py makemigrations --noinput
python3.8 manage.py migrate --noinput

echo "Collect Static..."
python3.8 manage.py collectstatic --noinput --clear