# Generated by Django 4.1.3 on 2023-01-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_parameters'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall',
            name='anchorsInCol',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wall',
            name='anchorsInRow',
            field=models.IntegerField(default=0),
        ),
    ]