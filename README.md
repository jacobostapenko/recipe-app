download files

to launch:
1. cd to app dir
2. run in console: $ python ./manage.py runserver

itll run locally

admin user creds:
username: user1 password: 123

to create user, either go into the django admin or add in shell using .create_user(username, password='_ex_')


to populate db, for now manually add stuff in through admin or through shell

from recipes.models import Recipes

p = Recipes(author='Dom V.', title = 'Meatballs', description = 'Combine ingredients, form into balls, brown, then place in oven')

p.save()
