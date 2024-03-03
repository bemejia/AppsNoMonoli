import propiedades.seedwork.presentacion.api as api
import json
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request
from flask import Response
from propiedades.modulos.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedades.modulos.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('vuelos', '/vuelos')

@bp.route('/propiedad-comando', methods=('POST',))
def crear_propiedad_asincrona():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(propiedad_dto.caracteristica, propiedad_dto.ciudad, propiedad_dto.id_propiedad, propiedad_dto.precio_max, propiedad_dto.precio_min, propiedad_dto.tamano_max, propiedad_dto.tamano_min, propiedad_dto.tipo)
    
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad-query', methods=('GET',))
@bp.route('/propiedad-query/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()
        
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]