from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Presentation
from .forms import AddedPresentationForm


class PresentationListView(ListView):
    model = Presentation
    template_name = "presentation/list_presentation_page.html"


class AddPresentationView(CreateView):
    model = Presentation
    form_class = AddedPresentationForm
    template_name = "presentation/add_presentation_page.html"
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class PresentationDetailView(DetailView):
    model = Presentation
    template_name = "presentation/detail_presentation_page.html"
