# Generated by Django 3.2.16 on 2022-11-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certification',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
