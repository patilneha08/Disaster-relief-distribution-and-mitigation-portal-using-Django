from django.contrib import admin
from .models import Donor, Volunteer, NGO, Rescue, General_Store, Grocerie, Hospital, Chemist
# Register your models here.

admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(NGO)
admin.site.register(Rescue)
admin.site.register(General_Store)
admin.site.register(Grocerie)
admin.site.register(Hospital)
admin.site.register(Chemist)

