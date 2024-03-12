import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

LEGAL_HOST = os.getenv("LEGAL_HOST", default="localhost")

FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_info_legal(root) -> typing.List["InfoLegal"]:
    info_legal_json = requests.get(f'{LEGAL_HOST}').json()
    info_legal = []

    for info_legal_obj in info_legal_json:
        info_legal.append(
            InfoLegal(
                fecha_creacion=datetime.strptime(info_legal_obj.get('fecha_creacion'), FORMATO_FECHA), 
                id=info_legal_obj.get('id'),
                tipo_propiedad=info_legal_obj.get('tipo_propiedad'),
                pais=info_legal_obj.get('pais'),
                departamento=info_legal_obj.get('departamento'),
                ciudad=info_legal_obj.get('ciudad'),
                direccion=info_legal_obj.get('direccion'),
                estado_legal=info_legal_obj.get('estado_legal'),
                tipo_contrato=info_legal_obj.get('tipo_contrato'),
                documento_legal=info_legal_obj.get('documento_legal'),
                valor_catastral=info_legal_obj.get('valor_catastral'),
                anio_construccion=info_legal_obj.get('anio_construccion'),
                superficie_terreno=info_legal_obj.get('superficie_terreno'),
                superficie_construida=info_legal_obj.get('superficie_construida'),
                nombre_propietario=info_legal_obj.get('nombre_propietario'),
                domicilio_propietario=info_legal_obj.get('domicilio_propietario'),
                uuid=info_legal_obj.get('uuid'),
            )
        )
    return info_legal

@strawberry.type
class Itinerario:
    # TODO Completar objeto strawberry para incluir los itinerarios
    ...

@strawberry.type
class InfoLegal:
    fecha_creacion: str
    id: str
    tipo_propiedad: str
    pais: str
    departamento: str
    ciudad: str
    direccion: str
    estado_legal: str
    tipo_contrato: str
    documento_legal: str
    valor_catastral: int
    anio_construccion: int
    superficie_terreno: int
    superficie_construida: int
    nombre_propietario: str
    domicilio_propietario: str
    uuid: str

@strawberry.type
class Reserva:
    id: str
    id_usuario: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    #itinerarios: typing.List[Itinerario]

@strawberry.type
class CatrastoRespuesta:
    mensaje: str
    codigo: int






