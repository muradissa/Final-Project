# Generated by Django 4.1.3 on 2022-11-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_heigth_wall_height'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optimizationType', models.IntegerField(default=0)),
                ('strategyType', models.IntegerField(default=0)),
                ('dimensionalType', models.IntegerField(default=0)),
            ],
        ),
    ]
