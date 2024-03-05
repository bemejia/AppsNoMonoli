from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.modulos.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.caracteristica = str(entidad.caracteristica)
        propiedad_dto.ciudad = str(entidad.ciudad)
        propiedad_dto.id_propiedad = int(entidad.id_propiedad)
        propiedad_dto.precio_max = int(entidad.precio_max)
        propiedad_dto.precio_min = int(entidad.precio_min)
        propiedad_dto.tamano_max = int(entidad.tamano_max)
        propiedad_dto.tamano_min = int(entidad.tamano_min)
        propiedad_dto.tipo = str(entidad.tipo)

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(dto.caracteristica, dto.ciudad, dto.id_propiedad, dto.precio_max, dto.precio_min, dto.tamano_max, dto.tamano_min, dto.tipo)
        return propiedad