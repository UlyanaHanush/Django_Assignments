# Generated by Django 4.1.7 on 2023-04-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_headline', models.CharField(max_length=255)),
                ('news_website', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
