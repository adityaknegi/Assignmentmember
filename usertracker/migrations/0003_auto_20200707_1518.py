# Generated by Django 3.0.8 on 2020-07-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertracker', '0002_auto_20200707_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]