# Generated by Django 5.0.3 on 2024-04-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_recipes_number_people_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='chfe_name',
            field=models.CharField(default=2, max_length=2048),
            preserve_default=False,
        ),
    ]