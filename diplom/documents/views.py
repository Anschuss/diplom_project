# from django.shortcuts import render
from django.views.generic import ListView
from .models import TenderDoc


class DocuTenderModelView(ListView):
    model = TenderDoc
    template_name = 'documents/tender_list_page.html'
