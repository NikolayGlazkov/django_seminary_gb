# Generated by Django 5.0.1 on 2024-01-25 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=10)),
                ('flip_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
