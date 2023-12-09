pip install -r requirements.txt

python3.9 manage.py squashmigrations

python3.9 manage.py makemigrations

python3.9 manage.py migrate

python manage.py createsuperuserwithpassword \
         --username admin \
         --password admin \
         --email admin@example.org \
         --preserve

python3.9 manage.py collectstatic