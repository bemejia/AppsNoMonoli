""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""
from datetime import datetime
import uuid
from propiedades_de_los_alpes.app_informacion_legal.aplicacion.dto import InfoLegalDTO
from seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador
from .dto import InfoLegal 

class MapeadorInfoLegalDTOJson(AppMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def externo_a_dto(self, externo: any) -> DTO:
        info_legal_dto = InfoLegalDTO(
            fecha_creacion=datetime.now().strftime(self._FORMATO_FECHA),
            id=uuid.uuid4().__str__(),
            tipo_propiedad=externo['tipo_propiedad'],
            pais=externo['pais'],
            departamento=externo['departamento'],
            ciudad=externo['ciudad'],
            direccion=externo['direccion'],
            estado_legal=externo['estado_legal'],
            tipo_contrato=externo['tipo_contrato'],
            documento_legal=externo['documento_legal'],
            valor_catastral=externo['valor_catastral'],
            anio_construccion=externo['anio_construccion'],
            superficie_terreno=externo['superficie_terreno'],
            superficie_construida=externo['superficie_construida'],
            nombre_propietario=externo['nombre_propietario'],
            domicilio_propietario=externo['domicilio_propietario'],
            uuid=externo['uuid']
        )
        return info_legal_dto
    
    def dto_a_externo(self, dto: DTO) -> any:
        pass

class MapeadorInfoLegal(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def entidad_a_dto(self, entidad: InfoLegal) -> InfoLegalDTO:
        pass
    
    def dto_a_entidad(self, dto: InfoLegalDTO) -> InfoLegal:
        info_legal_entity = InfoLegal(
        fecha_creacion=dto.fecha_creacion,
        tipo_propiedad=dto.tipo_propiedad,
        pais=dto.pais,
        departamento=dto.departamento,
        ciudad=dto.ciudad,
        direccion=dto.direccion,
        estado_legal=dto.estado_legal,
        tipo_contrato=dto.tipo_contrato,
        documento_legal=dto.documento_legal,
        valor_catastral=dto.valor_catastral,
        anio_construccion=dto.anio_construccion,
        superficie_terreno=dto.superficie_terreno,
        superficie_construida=dto.superficie_construida,
        nombre_propietario=dto.nombre_propietario,
        domicilio_propietario=dto.domicilio_propietario,
        uuid=dto.uuid
    )
        return info_legal_entity

    def obtener_tipo(self) -> type:
        return InfoLegal.__class__