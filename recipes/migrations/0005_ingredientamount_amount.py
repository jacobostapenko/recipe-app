# Generated by Django 3.2 on 2023-01-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20230108_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientamount',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
