from django.contrib import admin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from .models import Brand, CarModel, CarMalfunction, Malfunction, Glass, GlassType


class AdminBrand(admin.ModelAdmin):
    list_display = ('title', 'logo',)
    pass


class AdminCarModel(admin.ModelAdmin):
    pass


class AdminCarMalfunction(admin.ModelAdmin):
    pass


class AdminMalfunction(admin.ModelAdmin):
    pass


class AdminGlass(admin.ModelAdmin):
    list_display = ('name', 'get_types', 'get_car_models', 'country')
    pass


class AdminGlassType(admin.ModelAdmin):
    list_display = ('name',)
    pass


admin.site.register(Brand, AdminBrand)
admin.site.register(CarModel, AdminCarModel)
admin.site.register(CarMalfunction, AdminCarMalfunction)
admin.site.register(Malfunction, AdminMalfunction)
admin.site.register(Glass, AdminGlass)
admin.site.register(GlassType, AdminGlassType)

admin.site.site_header = "test black auto"
admin.site.site_title = "test black auto"
admin.site.index_title = "админ панель"
