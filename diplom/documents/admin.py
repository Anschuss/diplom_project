from django.contrib import admin
from .models import *


class RetailSailAdmin(admin.ModelAdmin):
    list_display = ('number_contract', 'customer', 'product', 'price')
    fields = ['number_contract', 'customer', 'document', 'price',
              'guarantee', 'type_product', 'product']


class TenderDocAdmin(admin.ModelAdmin):
    list_display = ('number_contract', 'clinic', 'customer', 'organizer', 'product', 'type_tender')
    fields = ['number_contract', 'customer', 'document', 'price', 'clinic',
              'guarantee', 'organizer', 'type_tender',
              'status', 'type_product', 'product', 'description']


class TypeProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name']


admin.site.register(TenderDoc, TenderDocAdmin),
admin.site.register(TenderType),
admin.site.register(Clinic),
admin.site.register(StatusTender),
admin.site.register(TypeProduct, TypeProductAdmin),
