from django.shortcuts import render
from django.views.generic import View, CreateView
from .models import LatestDox, TenderDoc
from .forms import AddedDocForm


class DoxView(View):

    def get(self, request, *args, **kwargs):
        dox = LatestDox.object.get_doc_for_page(kwargs['ct_model'])
        return render(request, 'documents/list_page.html', {"dox": dox})


class AddDoxView(CreateView):
    model = TenderDoc
    form_class = AddedDocForm
    template_name = "documents/add_tender_doc.html"
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)