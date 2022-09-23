from django.urls import path
from . import views

urlpatterns = [
   path('hello/', views.HelloView.as_view()),
   path('login/', views.login),
   path('signup/', views.signup),
   path('services/', views.service),
   path('cart/<int:pk>/', views.cart_toggle),
   path('cart/', views.cart_get),
   path('order/', views.order),
   path('logout/', views.logout_user),
   path('service/<int:pk>/', views.admin_service_delete),
   path('service/', views.admin_service),
]
