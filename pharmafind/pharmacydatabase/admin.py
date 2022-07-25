from django.contrib import admin

import pharmacydatabase
from .models import DrugType, Drug, Brand, DrugSet, Pharmacy

# Register your models here.

admin.site.register(DrugSet)
admin.site.register(Drug)
admin.site.register(Brand)
admin.site.register(DrugType)
admin.site.register(Pharmacy)