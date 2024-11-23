create a env for version control - python -m venv .env
env/Scripts/activate
pip install django
pip install djangorestframework
pip install django-cors-headers
django-admin startproject backend
cd backend
django-admin startapp list
write a code
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

optional 
python manage.py createsuperuser
