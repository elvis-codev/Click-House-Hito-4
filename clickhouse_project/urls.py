from django.contrib import admin
from django.urls import path
from static_pages import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('secreto/', views.secreto, name='secreto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('mis_propiedades/', views.mis_propiedades, name='mis_propiedades'),
    path('editar_propiedad/<int:propiedad_id>/', views.editar_propiedad, name='editar_propiedad'),
    path('eliminar_propiedad/<int:propiedad_id>/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('crear_propiedad/', views.crear_propiedad, name='crear_propiedad'),


    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

