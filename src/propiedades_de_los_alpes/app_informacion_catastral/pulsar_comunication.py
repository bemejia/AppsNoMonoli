import pulsar
from dotenv import load_dotenv
import os
from informacion_catastral.modulos.aplicacion.servicios import ServicioCatastro



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
    sr = ServicioCatastro()
    data_propiedad = str(sr.obtener_informacion_catastral(id))
    producer.send((data_propiedad).encode('utf-8'))
    
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


client = configurar_pulsar()
escucha_mensajes(client)