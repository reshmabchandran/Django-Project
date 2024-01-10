from django.contrib import admin
from .models import TenantDetails,PropertyDetails,UnitDetails

# Register your models here.

admin.site.register(TenantDetails)

admin.site.register(PropertyDetails)

admin.site.register(UnitDetails)
