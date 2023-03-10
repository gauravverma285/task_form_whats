# Generated by Django 3.2.16 on 2022-11-19 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('certification', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3)),
                ('instructor', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.job')),
            ],
        ),
    ]
