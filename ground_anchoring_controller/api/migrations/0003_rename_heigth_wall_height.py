# Generated by Django 4.1.3 on 2022-11-14 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_angel_wall_angle_rename_weigth_wall_width'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wall',
            old_name='heigth',
            new_name='height',
        ),
    ]
