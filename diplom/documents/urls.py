from django.urls import path
from .views import *

app_name = "documents"

urlpatterns = [
    path('<str:ct_model>/', DoxView.as_view(), name="sales")
]