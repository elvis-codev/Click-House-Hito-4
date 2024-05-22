import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clickhouse_project.settings")
django.setup()

from static_pages.models import Propiedad

def consultar_propiedades():
    with open("propiedades_por_comuna.txt", "w") as archivo:
        comunas = Propiedad.objects.values_list('comuna', flat=True).distinct()
        for comuna in comunas:
            archivo.write(f"Comuna: {comuna}\n")
            archivo.write("=" * 50 + "\n")
        
            propiedades = Propiedad.objects.filter(comuna=comuna)
            for propiedad in propiedades:
                archivo.write(f"Nombre: {propiedad.nombre}\n")
                archivo.write(f"Descripción: {propiedad.descripcion}\n")
                archivo.write("\n")
            archivo.write("\n")

if __name__ == "__main__":
    consultar_propiedades()
