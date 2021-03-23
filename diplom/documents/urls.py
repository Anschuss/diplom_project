from django.urls import path
from .views import *

app_name = "documents"

urlpatterns = [
    # path('tenders/', DocuTenderModelView.as_view(), name="tenders"),
    # path('retail/', DocuRetailModelView.as_view(), name="retail"),
    path('<str:ct_model>/', DoxView.as_view(), name="sales")
]