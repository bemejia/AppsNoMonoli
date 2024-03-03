from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = Long()

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()