# Generated by Django 2.1 on 2018-08-09 00:20

import django.core.validators
from django.db import migrations, models


def seed_locations(apps, schema_editor):
    location_model = apps.get_model('geo', 'Location')
    items = [
        {'city': 'Cincinnati', 'state': 'Ohio', 'zipcode': '41073'},
        {'city': 'Cincinnati', 'state': 'Ohio', 'zipcode': '41074'},
        {'city': 'Charlotte', 'state': 'North Carolina', 'zipcode': '28105'},
        {'city': 'Charlotte', 'state': 'North Carolina', 'zipcode': '28126'},
        {'city': 'Charlottesville', 'state': 'Virginia', 'zipcode': '22901'},
        {'city': 'Charlottesville', 'state': 'Virginia', 'zipcode': '22902'},
        {'city': 'Houston', 'state': 'Texas', 'zipcode': '77001'},
        {'city': 'Houston', 'state': 'Texas', 'zipcode': '77002'},
        {'city': 'Jersey City', 'state': 'New Jersey', 'zipcode': '07030'},
        {'city': 'Jersey City', 'state': 'New Jersey', 'zipcode': '07031'},
        {'city': 'Las Vegas', 'state': 'Nevada', 'zipcode': '89101'},
        {'city': 'Las Vegas', 'state': 'Nevada', 'zipcode': '89102'},
        {'city': 'Miami', 'state': 'Florida', 'zipcode': '33101'},
        {'city': 'Miami', 'state': 'Florida', 'zipcode': '33125'},
        {'city': 'New York', 'state': 'New York', 'zipcode': '10001'},
        {'city': 'New York', 'state': 'New York', 'zipcode': '10002'},
        {'city': 'Portland', 'state': 'Oregon', 'zipcode': '97201'},
        {'city': 'Portland', 'state': 'Oregon', 'zipcode': '97202'},
        {'city': 'San Diego', 'state': 'California', 'zipcode': '91911'},
        {'city': 'San Diego', 'state': 'California', 'zipcode': '91932'},
    ]

    for item in items:
        _ = location_model.objects.create(**item)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator("^[a-zA-Z' ]{3,15}$")])),
                ('state', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator("^[a-zA-Z' ]{4,14}$")])),
                ('zipcode', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$')])),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('city', 'state', 'zipcode')},
        ),
        migrations.RunPython(seed_locations)
    ]