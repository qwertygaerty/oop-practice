from django.urls import path
from . import views

urlpatterns = [
   path('hello/', views.HelloView.as_view()),
   path('login/', views.login),
   path('signup/', views.signup),
   path('services/', views.service),
   path('cart/<int:pk>/', views.cart_add),
   path('cart/', views.cart_get),
]
