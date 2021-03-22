from django.urls import path
from .views import *

app_name = "documents"

urlpatterns = [
    path('tenders/', DocuTenderModelView.as_view(), name="tenders"),
    path('retail/', DocuRetailModelView.as_view(), name="retail"),
]