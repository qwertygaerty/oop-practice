from django.conf import settings
from django.urls import path

from .views import home
from django.conf.urls.static import static

urlpatterns = [
    path('', home.index, name='index'),
    path('', home.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
