from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.modulos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedades.modulos.dominio.entidades import Aeropuerto, Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.id = str(entidad.id)

        itinerarios_dto = list()
        
        for itinerario in entidad.itinerarios:
            itinerarios_dto.extend(self._procesar_itinerario(itinerario))

        propiedad_dto.itinerarios = itinerarios_dto

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(dto.caracteristica, dto.ciudad, dto.id_propiedad, dto.precio_max, dto.precio_min, dto.tamano_max, dto.tamano_min, dto.tipo)
  
        
        return propiedad