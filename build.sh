pip install -r requirements.txt

python3.9 manage.py makemigrations

python3.9 manage.py migrate

python3.9 manage.py migrate custom

python manage.py createsuperuserwithpassword \
         --username admin \
         --password admin \
         --email admin@example.org \
         --preserve

python3.9 manage.py collectstatic