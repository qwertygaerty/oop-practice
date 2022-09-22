from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.login),
   path('signup/<int:pk>/', views.signup),
   path('hello/', views.HelloView.as_view(), name='hello'),
]
