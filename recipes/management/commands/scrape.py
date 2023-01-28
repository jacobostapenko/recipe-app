from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from recipe_scrapers import scrape_me
from pathlib import Path

from recipes.models import Ingredient, Recipe, RecipeIngredient

UNITS = ["unit", "ounce", "tablespoon", "teaspoon", "can", "cup", "cube", "thumb","box", "slice", "jar","milliliters",
         " g ", "clove"]

class Command(BaseCommand):
    help = 'Scrapes a specific website for recipes'

    def get_hellofresh(self):
        parent_dir = Path.cwd()
        file_path =  parent_dir.joinpath("recipes","management","hello_fresh_recipes.txt")
        with file_path.open() as f:
            file1 =  f.readlines()
        return [line.rstrip() for line in file1]

    def handle(self, *args, **options):
        recipes = self.get_hellofresh()
        for recipe in recipes:
            print("recipe!", recipe, "!")
            recipe_scraped = scrape_me(recipe)
            ingredient_map = {}
            ingredients = recipe_scraped.ingredients()
            for ing in ingredients:
                split_line = None
                for unit in UNITS:
                    if unit in ing:
                        split_line = ing.split(unit)
                        if len(split_line[0]) > 0:
                            a = split_line[0].strip()
                            #dealing with 1/4, 1/2, 3/4 ascii symbols
                            if ord(a[0]) in ([188,189,190]):
                                if a == 188:
                                    amount = float(1/4)
                                elif a == 189:
                                    amount = float(1/2)
                                else:
                                    amount = float(3/4)
                            else:
                                try:
                                    amount = float(a)
                                except:
                                    #for some reason, HelloFresh parser includes "2 * x" as ingredient amount and its wrong
                                    amount = 1
                        else:
                            amount = 1
                        if unit == "unit":
                            unit = ""
                        ingredient_map[split_line[1].lower().strip()] = (amount, unit)
                        break

                if split_line is None and ("Pepper" not in ing) and ("Salt" not in ing):
                    print("Cant split", ing)

            ingriedent_array = ingredient_map.keys()
            existing_ingredients = Ingredient.objects.filter(name__in=ingriedent_array)
            existing_ingredient_list = existing_ingredients.values_list("name", flat=True)
            title = recipe_scraped.title().strip()

            author = User.objects.first()
            if not Recipe.objects.filter(title=title).exists():
                Recipe(url=recipe, title =title, author = author).save()
            else:
                print("already have recipe " + title + "in the db")
                continue

            recipe_object = Recipe.objects.get(url=recipe)
            for i, v in ingredient_map.items():
                a,unit = v
                ingredient_object = None
                if i not in existing_ingredient_list:
                    ingredient_object = Ingredient(name=i)
                    ingredient_object.save()


                if ingredient_object is None:
                    ingredient_object = existing_ingredients.filter(name = i).first()
                RecipeIngredient(recipe=recipe_object, ingredient = ingredient_object, amount=a,unit=unit).save()

