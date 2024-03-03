import pulsar
from pulsar.schema import *

from propiedades.modulos.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload
from propiedades.modulos.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from propiedades.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            caracteristica=str(evento.caracteristica),
            ciudad=str(evento.ciudad),
            id_propiedad=str(evento.id_propiedad),
            precio_max=int(evento.precio_max),
            precio_min=int(evento.precio_min),
            tamano_max=int(evento.tamano_max),
            tamano_min=int(evento.tamano_min),
            tipo=int(evento.tipo)
        )
        evento_integracion = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadCreada))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearPropiedadPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))
