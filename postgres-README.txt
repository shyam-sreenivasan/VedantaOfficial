# Starting server
cd ~/.start_postgres

# Creating user
Create user:
createuser --interactive --pwprompt -p 19999

# Creating database
Create database:
CREATE DATABASE vvpdb;

# Creating user on django login
python manage.by createsuperuser

# for new deployment on heroku
https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1

https://simpleit.rocks/python/django/use-postgresql-database-in-heroku-for-testing-django/