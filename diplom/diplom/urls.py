from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginuser.urls', namespace='login')),
    path('documents/', include('documents.urls', namespace='doc')),
    path('presentation/', include('presentation.urls', namespace='presentation')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
