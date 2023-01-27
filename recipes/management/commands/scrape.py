from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from recipe_scrapers import scrape_me
from pathlib import Path

from recipes.models import Ingredient, Recipe, RecipeIngredient

UNITS = ["unit", "ounce", "tablespoon", "teaspoon"]

class Command(BaseCommand):
    help = 'Scrapes a specific website for recipes'
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
    def get_hellofresh(self):
        parent_dir = Path.cwd()
        file_path =  parent_dir.joinpath("recipes","management","hello_fresh_recipes.txt")
        with file_path.open() as f:
            file1 =  f.readlines()
        return [line.rstrip() for line in file1]

    def handle(self, *args, **options):
        recipes = self.get_hellofresh()
        print(recipes)
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
                            print(type(a), ord(a[0]))
                            if ord(a[0]) in ([188,189,190]):
                                if a == 188:
                                    amount = float(1/4)
                                elif a == 189:
                                    amount = float(1/2)
                                else:
                                    amount = float(3/4)
                            else:
                                amount = float(a)
                        else:
                            amount = 1
                        ingredient_map[split_line[1].lower()] = (amount, unit)

                if split_line is None:
                    print("Cant split", ing)

            ingriedent_array = ingredient_map.keys()
            existing_ingredients = Ingredient.objects.filter(name__in=ingriedent_array)
            print(recipe_scraped)
            title = recipe_scraped.title()
            print("parsed",recipe)
            print("title", title)
            author = User.objects.first()
            #TODO: dont recreate recipes
            if not Recipe.objects.filter(title=title).exists():
                Recipe(url=recipe, title =title, author = author).save()
            else:
                print("already have recipe " + title + "in the db")
                continue
            recipe_object = Recipe.objects.get(url=recipe)
            print(ingredient_map)
            for i, v in ingredient_map.items():
                print(i)
                a,unit = v
                if i not in existing_ingredients:
                    print("inserting ingredient", i)
                    Ingredient(name=i).save()

                ingredient_object = existing_ingredients.filter(name = i).first()
                print(ingredient_object, i)
                RecipeIngredient(recipe=recipe_object, ingredient = ingredient_object, amount=a,unit=unit).save()

