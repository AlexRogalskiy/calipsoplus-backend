# Generated by Django 2.0.2 on 2018-06-07 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20180529_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='calipsocontainer',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='historicalcalipsocontainer',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
