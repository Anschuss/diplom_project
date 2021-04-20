from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import *

app_name = "documents"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)