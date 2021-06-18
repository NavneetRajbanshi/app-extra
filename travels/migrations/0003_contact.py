# Generated by Django 3.2.4 on 2021-06-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_traveler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
