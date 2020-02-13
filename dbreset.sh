#!/bin/sh
cd review
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations review
python manage.py migrate
python manage.py createsuperuser
./runserver.sh