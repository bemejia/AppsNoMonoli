import pulsar, _pulsar
from pulsar.schema import *
from dotenv import load_dotenv
import os
import aiopulsar

# Carga las variables de entorno del archivo .env
load_dotenv()

def configurar_pulsar():
    service_url = 'pulsar+ssl://pulsar-aws-useast1.streaming.datastax.com:6651'
    token = os.getenv('PULSAR_TOKEN')
    client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))
    
    return client

def publicar_mensaje_catasto(client, id):
    # Definir topico
    producer = client.create_producer('persistent://nomonoliticas/default/catastro')
    # Enviar mensaje
    #sr = ServicioAuditoria()
    #data_propiedad = str(sr.obtener_informacion_catastral(id))
    producer.send((f"Servico Desplegado Correctamente {id}").encode('utf-8'))
    
def publicar_mensaje_general(client, topico, mensaje):
    # Definir topico
    producer = client.create_producer(f'persistent://nomonoliticas/default/{topico}')
    # Enviar mensaje
    mensaje = str(mensaje)
    producer.send(mensaje.encode('utf-8'))

def escucha_mensajes(client):
    consumer = client.subscribe('persistent://nomonoliticas/default/catastro', 'test-subscription')
    waitingForMsg = True
    while waitingForMsg:
        try:
            msg = consumer.receive()
            print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
            id_propiedad = int(msg.data())
            publicar_mensaje_catasto(client, id_propiedad)
            consumer.acknowledge(msg)
            
        except:
            print("Still waiting for a message...");
    client.close()

async def suscribirse_a_topico(topico, suscripcion, handler):
        token = os.getenv('PULSAR_TOKEN')
        options = {
        'authentication': pulsar.AuthenticationToken(token),
        }
        print(f"Suscribiendose al tópico de eventos... {topico}")
        async with aiopulsar.connect('pulsar+ssl://pulsar-aws-useast1.streaming.datastax.com:6651', **options) as client:
            async with client.subscribe(
                   f'persistent://nomonoliticas/default/{topico}', suscripcion) as consumidor:
                        while True:
                            mensaje = await consumidor.receive()
                            print(mensaje)
                            datos = mensaje.value()
                            print(f'Evento recibido: {datos}')
                            handler(topico, datos.decode('utf-8'))
                            await consumidor.acknowledge(mensaje)  


