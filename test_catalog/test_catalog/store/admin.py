from django.contrib import admin

from .models import Customer, Category, Product


class AdminCategory(admin.ModelAdmin):
    pass


class AdminCustomer(admin.ModelAdmin):
    pass


admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Product, AdminCustomer)
