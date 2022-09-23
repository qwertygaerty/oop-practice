from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.login),
   path('signup/', views.signup),
   path('hello/', views.HelloView.as_view()),
]
