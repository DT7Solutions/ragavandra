# ragavandra

# krystabackend

# magsmen
#django

#install env
#pip install virtualenv
# create virtual environment
#python -m venv env-ragavendra

# activate virtual environmentcd
#env-ragavendra\Scripts\activate

# install libs
pip freeze > requirements.txt 
pip install -r requirements.txt

# create django  project
Django-admin startproject "PROJECTNAME"

# create django app 
python manage.py startapp "APP NAME"

# create super user 
python manage.py createsuperuser
# migration process 
python manage.py makemigrations 

# run migrations 
python manage.py migrate 

# Run project or applications
python manage.py runserver

# note:
# pip freeze > requirements.txt 

<!-- #admin details -->
<!-- username:raghavendra
password: 123456 -->

<!-- url:-4a6a2ee7-4431-4e22-9913-73930326f7f9 -->
 http://127.0.0.1:8000/4a6a2ee7-4431-4e22-9913-73930326f7f9 :- call back url 
 8f08d35c-d4a3-4ce0-bec8-db786e9a100f :- token