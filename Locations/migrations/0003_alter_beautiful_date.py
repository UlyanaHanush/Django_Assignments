# Generated by Django 4.1.7 on 2023-04-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locations', '0002_rename_beautiful_locations_beautiful'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautiful',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
