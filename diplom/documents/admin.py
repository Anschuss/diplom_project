from django.contrib import admin
from .models import TenderDoc, TenderType, Clinic


admin.site.register(TenderDoc),
admin.site.register(TenderType),
admin.site.register(Clinic)
