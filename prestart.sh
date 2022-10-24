#! /usr/bin/env bash

# Let the DB start
sleep 10;


python /app/manage.py makemigrations
python /app/manage.py migrate
echo yes | python /app/manage.py collectstatic
python /app/fill_db.py