# Generated by Django 3.2 on 2023-01-08 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredientamount'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ingredient',
            table='ingredient',
        ),
        migrations.AlterModelTable(
            name='ingredientamount',
            table='ingredientamount',
        ),
        migrations.AlterModelTable(
            name='recipe',
            table='recipe',
        ),
    ]
