#!/bin/bash

# Build the project
echo "Building the project..."

python3.9 --version

python --version

echo "installing pipenv"
python3.9 -m pip install virtualenv

echo "making pip now"

python3.9 -m virtualenv myenv

echo "pipenv activating -----------"

source myenv/bin/activate 

echo "pip installing requirements ----------"


python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear