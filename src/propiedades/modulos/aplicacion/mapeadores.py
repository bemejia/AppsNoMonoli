from propiedades.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedades.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedades.modulos.dominio.entidades import Propiedad
from .dto import PropiedadDTO

class MapeadorPropiedadDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        caracteristica = str(entidad.caracteristica)
        ciudad = str(entidad.ciudad)
        id_propiedad = int(entidad.id_propiedad)
        precio_max = str(entidad.precio_max)
        precio_min = str(entidad.precio_min)
        tamano_max = str(entidad.tamano_max)
        tamano_min = str(entidad.tamano_min)
        tipo = str(entidad.tipo)
        
        return PropiedadDTO(caracteristica, ciudad, id_propiedad, precio_max, precio_min, tamano_max, tamano_min, tipo)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        return propiedad