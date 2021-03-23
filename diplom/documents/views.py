from django.shortcuts import render
from django.views.generic import ListView, View
from .models import TenderDoc, RetailSales, LatestDox


# class DocuTenderModelView(ListView):
#     model = TenderDoc
#     template_name = 'documents/list_page.html'
#
#
# class DocuRetailModelView(ListView):
#     model = RetailSales
#     template_name = 'documents/list_page.html'

class DoxView(View):

    def get(self, request, *args, **kwargs):
        dox  = LatestDox.object.get_doc_for_page(kwargs['ct_model'])
        return render(request, 'documents/list_page.html', {"dox": dox})
