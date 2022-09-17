from django.conf import settings
from django.urls import path

from .views import home
from django.conf.urls.static import static

urlpatterns = [
    path('', home.index, name='index'),
    path('mailfunction/', home.malfunction, name='mailfunction'),
    path('glass/', home.glass, name='glass'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
