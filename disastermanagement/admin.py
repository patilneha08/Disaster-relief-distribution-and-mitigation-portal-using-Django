from django.contrib import admin
from .models import Donor, Volunteer, NGO
# Register your models here.

admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(NGO)

