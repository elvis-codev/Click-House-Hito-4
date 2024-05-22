from .models import Usuario, Propiedad, Region, Comuna

def crear_usuario(nombres, apellidos, rut, direccion, telefono, correo, tipo_usuario):
    return Usuario.objects.create(nombres=nombres, apellidos=apellidos, rut=rut, direccion=direccion, telefono=telefono, correo=correo, tipo_usuario=tipo_usuario)

def listar_propiedades_por_comuna(comuna):
    return Propiedad.objects.filter(comuna=comuna)

def generar_solicitud_arriendo(arrendatario_id, propiedad_id):
    arrendatario = Arrendatario.objects.get(id=arrendatario_id)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    arrendatario.propiedades_interes.add(propiedad)

def publicar_propiedad(arrendador_id, nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    arrendador = Arrendador.objects.get(id=arrendador_id)
    propiedad = Propiedad.objects.create(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, estacionamientos=estacionamientos, habitaciones=habitaciones, banos=banos, direccion=direccion, comuna=comuna, tipo_inmueble=tipo_inmueble, precio_arriendo=precio_arriendo)
    arrendador.propiedades_publicadas.add(propiedad)

def eliminar_propiedad(arrendador_id, propiedad_id):
    arrendador = Arrendador.objects.get(id=arrendador_id)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    arrendador.propiedades_publicadas.remove(propiedad)
    propiedad.delete()

def editar_propiedad(propiedad_id, nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    propiedad = Propiedad.objects.get(id=propiedad_id)
    propiedad.nombre = nombre
    propiedad.descripcion = descripcion
    propiedad.m2_construidos = m2_construidos
    propiedad.m2_totales = m2_totales
    propiedad.estacionamientos = estacionamientos
    propiedad.habitaciones = habitaciones
    propiedad.banos = banos
    propiedad.direccion = direccion
    propiedad.comuna = comuna
    propiedad.tipo_inmueble = tipo_inmueble
    propiedad.precio_arriendo = precio_arriendo
    propiedad.save()



# Agregando Datos Hito 2
class RegionService:
    @staticmethod
    def get_all_regions():
        return Region.objects.all()

    @staticmethod
    def get_region_by_id(region_id):
        return Region.objects.get(pk=region_id)

class ComunaService:
    @staticmethod
    def get_all_comunas():
        return Comuna.objects.all()

    @staticmethod
    def get_comunas_by_region(region_id):
        return Comuna.objects.filter(region_id=region_id)

class TipoInmuebleService:
    @staticmethod
    def get_all_tipos_inmueble():
        return TipoInmueble.objects.all()

class InmuebleService:
    @staticmethod
    def create_inmueble(tipo_id, comuna_id):
        tipo = TipoInmueble.objects.get(pk=tipo_id)
        comuna = Comuna.objects.get(pk=comuna_id)
        return Inmueble.objects.create(tipo=tipo, comuna=comuna)

    @staticmethod
    def get_inmuebles_by_comuna(comuna_id):
        return Inmueble.objects.filter(comuna_id=comuna_id)

    @staticmethod
    def get_inmuebles_by_tipo(tipo_id):
        return Inmueble.objects.filter(tipo_id=tipo_id)