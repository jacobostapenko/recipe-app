
## Clone project:

```git clone https://github.com/jacobostapenko/recipe-app.git```

Next set up a virtualenv to deal with dependencies

```python3.8 -m venv recipe-venv```

Remember to add the venv to you .git-ignore. i.e. add `recipe-venv/` to the file

Start your virtual env using
```source recipe-venv/bin/activate```

You will see yourselv in the virtualenv if `(recipe-venv)` appears at the beginning of your terminal line

install the dependencies needed via `pip3.8 install -r requirements.txt`

You can check if the install was successful using `django-admin --version` and 3.2 should appear.

## To Update `Requirements.txt`:
You can simply run `pip install XXX` where `XXX` is the package you want to use. Next, run
 `diff -u requirements.txt <(pip freeze)` and see what has changed in the file and make those updates

## Setup DB

Install Postgres 14 from here: https://www.postgresql.org/download/
Run Postgress and click on the default DB created for you. This should open a Terminal shell. Run the commands below to
create the DB needed

To add psql to the path of the virtual environment, run the following commands(for regular installation of postgreSQL):

export PATH="/Library/PostgreSQL/14/bin:$PATH"

make sure to change version(number after PostgreSQL/) if your postgres version is different

```CREATE DATABASE recipes;```

```
CREATE USER admin WITH PASSWORD 'password';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET timezone TO 'UTC';
```
and then leave via `exit`.



To udpate db / migrate before you run the server:

open up a shell, and go into your virtual environment. Change directories to end up in the recipe-app dir. Run the commands below:

./manage.py makemigration

./manage.py migrate


## Accessing the Admin Console
TODO: add this info and create mock data for DB


to launch:
1. cd to app dir
2. run in console: $ python ./manage.py runserver

itll run locally

admin user creds:
username: user1 password: password

to create user, either go into the django admin or add in shell using .create_user(username, password='_ex_')


to populate db, for now manually add stuff in through admin 


