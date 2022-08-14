from django.contrib import admin

# Register your models here.
from farm.models import login,farmer,research_agro,drone_operator,kvk,warehouse,registration

admin.site.register(login)
admin.site.register(farmer)
admin.site.register(research_agro)
admin.site.register(drone_operator)
admin.site.register(kvk)
admin.site.register(warehouse)
admin.site.register(registration)