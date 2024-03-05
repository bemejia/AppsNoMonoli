from propiedades_de_los_alpes.app_informacion_legal.aplicacion.servicios import ServicioInfoLegal
import pulsar
from dotenv import load_dotenv
import os


# Carga las variables de entorno del archivo .env
load_dotenv()

def configurar_pulsar():
    service_url = 'pulsar+ssl://pulsar-aws-useast1.streaming.datastax.com:6651'
    token = os.getenv('PULSAR_TOKEN')
    client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))
    
    return client


def publicar_mensaje_legal(client, ids):
    # Definir topico
    producer = client.create_producer('persistent://nomonoliticas/default/legal')
    # Enviar mensaje
    print("Enviando mensaje:",ids)
    data_propiedad = str(ids)
    print(producer.send((data_propiedad).encode('utf-8')))


client = configurar_pulsar()