# Generated by Django 4.1 on 2022-08-15 13:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_drone_operator_adhaar_number_farmer_adhaar_number_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='login',
            managers=[
                ('Auth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='role',
            field=models.CharField(choices=[('Farmer', 'Farmer'), ('Researcher', 'Researcher'), ('Agro-scientist', 'Agro-scientist'), ('Drone Operator', 'Drone Operator'), ('KVK', 'KVK'), ('Warehouse', 'Warehouse'), ('Food Processor', 'Food Processor'), ('Distributer', 'Distributer'), ('Retailer', 'Retailer'), ('Others', 'Others')], max_length=80),
        ),
    ]
