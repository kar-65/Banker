from django.contrib import admin

# Register your models here.
from . models import Country
from . models import City
admin.site.register(Country)
admin.site.register(City)