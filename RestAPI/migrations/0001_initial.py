# Generated by Django 2.1 on 2018-08-10 09:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=4, max_digits=8)),
                ('lon', models.DecimalField(decimal_places=4, max_digits=8)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=4, max_digits=8), size=50)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RestAPI.Location')),
            ],
        ),
    ]
