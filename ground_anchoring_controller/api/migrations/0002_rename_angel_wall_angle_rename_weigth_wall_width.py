# Generated by Django 4.1.3 on 2022-11-14 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wall',
            old_name='angel',
            new_name='angle',
        ),
        migrations.RenameField(
            model_name='wall',
            old_name='weigth',
            new_name='width',
        ),
    ]
