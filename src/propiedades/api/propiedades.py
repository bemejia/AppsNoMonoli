import propiedades.seedwork.presentacion.api as api
import json
from propiedades.modulos.aplicacion.servicios import ServicioReserva
from propiedades.modulos.aplicacion.dto import ReservaDTO
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request
from flask import Response
from propiedades.modulos.aplicacion.mapeadores import MapeadorReservaDTOJson
from propiedades.modulos.aplicacion.comandos.crear_reserva import CrearReserva
from propiedades.modulos.aplicacion.queries.obtener_reserva import ObtenerReserva
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('vuelos', '/vuelos')

@bp.route('/reserva-comando', methods=('POST',))
def reservar_asincrona():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        comando = CrearReserva(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva-query', methods=('GET',))
@bp.route('/reserva-query/<id>', methods=('GET',))
def dar_reserva_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerReserva(id))
        map_reserva = MapeadorReservaDTOJson()
        
        return map_reserva.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]