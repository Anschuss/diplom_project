from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "documents"

urlpatterns = [
    path('', VoidView.as_view(), name="void"),
    path('tenders/', TenderListView.as_view(), name="sales"),
    path('tenders/add', AddTenderView.as_view(), name="add_tender"),
    path('tenders/<str:slug>/', TenderDetailView.as_view(), name="detail")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)