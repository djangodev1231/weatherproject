# Generated by Django 2.1 on 2018-08-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0002_weather_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]