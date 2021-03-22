# from django.shortcuts import render
from django.views.generic import ListView
from .models import TenderDoc, RetailSales


class DocuTenderModelView(ListView):
    model = TenderDoc
    template_name = 'documents/list_page.html'


class DocuRetailModelView(ListView):
    model = RetailSales
    template_name = 'documents/list_page.html'
