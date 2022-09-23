from django.contrib import admin

# Register your models here.


from .models import User, Role, Service, Cart, Order

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Service)
admin.site.register(Cart)
admin.site.register(Order)
