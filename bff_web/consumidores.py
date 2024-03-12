import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from . import utils
import os
from dotenv import load_dotenv
load_dotenv()
async def suscribirse_a_topico(topico: str, suscripcion: str, schema: str, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared, eventos=[]):
    try:
        async with aiopulsar.connect(f'pulsar+ssl://{utils.broker_host()}:6651', authentication=pulsar.AuthenticationToken(os.getenv("PULSAR_TOKEN"))) as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}')
        traceback.print_exc()