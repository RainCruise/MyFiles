from django.contrib import admin
from .models import Infomation_dars, Infomation_szqt

# Register your models here.
class Infomation_darsAdmin(admin.ModelAdmin):
    list_display = ('name', 'eamil_address' )

class Infomation_szqtAdmin(admin.ModelAdmin):
    list_display = ('name', 'eamil_address' )

admin.site.register(Infomation_dars, Infomation_darsAdmin)
admin.site.register(Infomation_szqt, Infomation_szqtAdmin)