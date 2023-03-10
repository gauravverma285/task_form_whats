# Generated by Django 3.2.16 on 2022-11-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('countary', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('current_address', models.CharField(max_length=200)),
                ('project', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('number', models.IntegerField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
