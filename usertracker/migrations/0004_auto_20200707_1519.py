# Generated by Django 3.0.8 on 2020-07-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertracker', '0003_auto_20200707_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.CharField(default='', max_length=50),
        ),
    ]