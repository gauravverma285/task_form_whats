# Generated by Django 3.2.16 on 2022-11-28 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221117_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='job',
        ),
    ]
