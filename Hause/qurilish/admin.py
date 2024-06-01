from django.contrib import admin
# Register your models here.
from . models import Region, Organizaytion, Building


admin.site.register(Region)
admin.site.register(Organizaytion)
admin.site.register(Building)