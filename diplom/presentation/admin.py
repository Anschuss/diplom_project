from django.contrib import admin
from .models import *


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('number_tender', 'status')
    fields = ['number_tender', 'status', 'description', 'file_presentation']


admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Status)
