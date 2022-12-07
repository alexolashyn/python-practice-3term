# Generated by Django 4.1.3 on 2022-11-13 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('registration_number', models.CharField(max_length=200)),
                ('bought_at', models.DateField(default=datetime.date(2022, 11, 13))),
                ('repaired_at', models.DateField(default=datetime.date(2022, 11, 13))),
                ('car_mileage', models.PositiveIntegerField(default=1000)),
            ],
        ),
    ]
