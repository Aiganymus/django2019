# Generated by Django 2.2.5 on 2019-09-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='is_creator',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='is_executor',
            field=models.BooleanField(default=False),
        ),
    ]
