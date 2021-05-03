from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import *

app_name = "documents"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name="update")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)