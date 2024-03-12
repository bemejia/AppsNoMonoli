from informacion_propiedades.modulos.dominio.entidades import InformacionPropiedad
from informacion_propiedades.modulos.infraestructura.repositorio import RepositorioInformacionPropiedad

def ejecutar_comando(data):

    info_propiedad = InformacionPropiedad()
    info_propiedad.caracteristica = data['caracteristica']
    info_propiedad.ciudad = data['ciudad']
    info_propiedad.id_propiedad = data['id_propiedad']
    info_propiedad.precio_max = data['precio_max']
    info_propiedad.precio_min = data['precio_min']
    info_propiedad.tamano_max = data['tamano_max']
    info_propiedad.tamano_min = data['tamano_min']
    info_propiedad.tipo = data['tipo']

    repositorio = RepositorioInformacionPropiedad()
    repositorio.crear_propiedad(info_propiedad)
