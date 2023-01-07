
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


to launch:
1. cd to app dir
2. run in console: $ python ./manage.py runserver

itll run locally

admin user creds:
username: user1 password: 123

to create user, either go into the django admin or add in shell using .create_user(username, password='_ex_')


to populate db, for now manually add stuff in through admin 


