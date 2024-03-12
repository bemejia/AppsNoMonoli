import pulsar
from pulsar.schema import *

from . import utils
import os
class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):
        print("Este es el mensaje",mensaje)
        cliente = pulsar.Client(f'pulsar+ssl://{utils.broker_host()}:6651', authentication=pulsar.AuthenticationToken(os.getenv("PULSAR_TOKEN")))
        publicador = cliente.create_producer(topico)
        publicador.send(mensaje)
        cliente.close()
