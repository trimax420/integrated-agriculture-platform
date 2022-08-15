import email
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class farmer(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    passno = models.CharField(max_length=80)
    surnum = models.CharField(max_length=80)
    landsize = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    landtype = models.CharField(max_length=80)

class research_agro(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    edu_quali = models.CharField(max_length=80)
    passyear = models.CharField(max_length=80)
    uni_name = models.CharField(max_length=80)
    org_name = models.CharField(max_length=80)
    student_name = models.CharField(max_length=80)
    emp_id = models.CharField(max_length=80)
    message = models.CharField(max_length=80)

class drone_operator(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    licensenum = models.CharField(max_length=80)
    message = models.CharField(max_length=80)

class kvk(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    kvk_id = models.CharField(max_length=80)
    message = models.CharField(max_length=80)

class warehouse(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    crn = models.CharField(max_length=80)
    gstin = models.CharField(max_length=80)
    cin = models.CharField(max_length=80)
    message = models.CharField(max_length=80)

class login(models.Model):
    CHOICES = (
        ('Farmer', 'Farmer'),
        ('Researcher', 'Researcher'),
        ('Agro-scientist', 'Agro-scientist'),
        ('Drone Operator', 'Drone Operator'),
        ('KVK', 'KVK'),
        ('Warehouse','Warehouse'),
        ('Food Processor','Food Processor'),
        ('Distributer','Distributer'),
        ('Retailer','Retailer'),
        ('Others','Others')
    )
    userid = models.CharField(max_length=80)
    password = models.CharField(max_length= 80)
    role = models.CharField(max_length=80,choices=CHOICES)

class registration(models.Model):
    CHOICES = (
        ('Farmer', 'Farmer'),
        ('Researcher', 'Researcher'),
        ('Agro-scientist', 'Agro-scientist'),
        ('Drone Operator', 'Drone Operator'),
        ('KVK', 'KVK'),
        ('Warehouse','Warehouse'),
        ('Food Processor','Food Processor'),
        ('Distributer','Distributer'),
        ('Retailer','Retailer'),
        ('Others','Others')
    )
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    emailid = models.CharField(max_length=80)
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    address = models.CharField(max_length=80)
    role = models.CharField(max_length=80,choices=CHOICES)

class others(models.Model):
    adhaar_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,12}$')])
    message = models.CharField(max_length=80)
