from django.contrib import admin
from .models import Usuario, Propiedad, Region, Comuna

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo','rut','tipo_usuario')  
    list_filter = ('tipo_usuario',)  

    def nombre_completo(self, obj):
        return f"{obj.nombres} {obj.apellidos}"

    nombre_completo.short_description = 'Nombres'  


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comuna', 'tipo_inmueble', 'precio_arriendo')
    list_filter = ('comuna', 'tipo_inmueble')



# Agregando Datos Hito 2
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region')
    list_filter = ('region',)

