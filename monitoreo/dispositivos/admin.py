from django.contrib import admin

# Register your models here.

from .models import Dispositivos

@admin.register(Dispositivos)
class DispositivosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'consumo_maximo', 'estado')
    list_filter = ('consumo_maximo', 'estado')
    search_fields = ('nombre',)



