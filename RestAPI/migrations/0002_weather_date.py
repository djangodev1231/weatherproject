# Generated by Django 2.1 on 2018-08-10 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]