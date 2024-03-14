from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("users.urls", namespace='user')),
    path('', include('person.urls', namespace='person'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
