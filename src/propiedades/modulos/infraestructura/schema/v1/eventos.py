from pulsar.schema import *
from propiedades.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    caracteristica = String()
    ciudad = String()
    id_propiedad = String()
    precio_max = Long()
    precio_min = Long()
    tamano_max = Long()
    tamano_min = Long()
    tipo = String()

class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()