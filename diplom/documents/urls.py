from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "documents"

urlpatterns = [
    path('<str:ct_model>/', DoxView.as_view(), name="sales"),
    path('<str:ct_model>/add', AddDoxView.as_view(), name="add")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

