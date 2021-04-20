from django.shortcuts import render
from django.views.generic import View, CreateView, DetailView, ListView
from .models import LatestDox, TenderDoc, StatusTender
from .forms import AddedTenderForm


class VoidView(View):
    pass


class TenderListView(ListView):
    model = TenderDoc
    template_name = "documents/list_page.html"


class TenderDetailView(DetailView):
    model = TenderDoc
    template_name = "documents/detail_page.html"


class AddTenderView(CreateView):
    model = TenderDoc
    form_class = AddedTenderForm
    template_name = "documents/add_tender_doc.html"
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)



