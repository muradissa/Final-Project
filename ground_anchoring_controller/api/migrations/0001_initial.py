# Generated by Django 4.1.3 on 2022-11-13 19:44

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anchor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0, unique=True)),
                ('anchor_is_help', models.BooleanField(default=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=api.models.generate_unique_string_code, max_length=8, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('heigth', models.IntegerField(default=20)),
                ('weigth', models.IntegerField(default=50)),
                ('angel', models.IntegerField(default=90)),
                ('number_of_anchors', models.IntegerField(default=100)),
                ('v', models.FloatField(default=0.1)),
                ('c', models.IntegerField(default=1)),
                ('e', models.IntegerField(default=30)),
                ('i', models.IntegerField(default=104)),
            ],
        ),
    ]
