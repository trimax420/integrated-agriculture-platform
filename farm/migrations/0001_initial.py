# Generated by Django 4.1 on 2022-08-14 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drone_operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licensenum', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passno', models.CharField(max_length=80)),
                ('surnum', models.CharField(max_length=80)),
                ('landsize', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('landtype', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='kvk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvk_id', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('role', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('emailid', models.CharField(max_length=80)),
                ('adhaar_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('address', models.CharField(max_length=80)),
                ('role', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='research_agro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_quali', models.CharField(max_length=80)),
                ('passyear', models.CharField(max_length=80)),
                ('uni_name', models.CharField(max_length=80)),
                ('org_name', models.CharField(max_length=80)),
                ('student_name', models.CharField(max_length=80)),
                ('emp_id', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.CharField(max_length=80)),
                ('gstin', models.CharField(max_length=80)),
                ('cin', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=80)),
            ],
        ),
    ]
