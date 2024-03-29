# Generated by Django 4.2.dev20221029113422 on 2022-11-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_alter_auto_bought_at_alter_auto_repaired_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='bought_at',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='auto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='registration_number',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='auto',
            name='repaired_at',
            field=models.CharField(max_length=10),
        ),
    ]
