from django.shortcuts import render
from django.views.generic import View
from .models import LatestDox


class DoxView(View):

    def get(self, request, *args, **kwargs):
        dox = LatestDox.object.get_doc_for_page(kwargs['ct_model'])
        return render(request, 'documents/list_page.html', {"dox": dox})
