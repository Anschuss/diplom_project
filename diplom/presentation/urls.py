from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "presentation"

urlpatterns = [
    path('all/', PresentationListView.as_view(), name="presentation_list"),
    path('add/', AddPresentationView.as_view(), name="add_presentation"),
    path('<str:slug>/', PresentationDetailView.as_view(), name="detail_presentation"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)