from django.contrib import admin

from .models import Brand, CarModel, CarMalfunction, Malfunction


# Register your models here.

class AdminBrand(admin.ModelAdmin):
    list_display = ('title', 'logo',)

    pass


class AdminCarModel(admin.ModelAdmin):
    pass


class AdminCarMalfunction(admin.ModelAdmin):
    pass


class AdminMalfunction(admin.ModelAdmin):
    pass


admin.site.register(Brand, AdminBrand)
admin.site.register(CarModel, AdminCarModel)
admin.site.register(CarMalfunction, AdminCarMalfunction)
admin.site.register(Malfunction, AdminMalfunction)
