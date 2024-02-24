from google.cloud import pubsub_v1
from informacion_catastral.modulos.aplicacion.servicios import ServicioCatastro
import base64



def dar_informacion_catastro_callback(message):
        project_id = "apps-no-monoliticas-415223"
        publisher = pubsub_v1.PublisherClient()
        topic_name = "resultados_catastro"
        topic_path = publisher.topic_path(project_id,  topic_name)
        print(f'Mensaje recibido: {message}')
        try:
            if 'data' in message:
                # Decodifica los datos de base64 a una cadena de texto.
                message_id = base64.b64decode(message['data']).decode('utf-8')
                
                sr = ServicioCatastro()
        
                data_propiedad = sr.obtener_informacion_catastral(message_id)
                future = publisher.publish(topic_path, data=str(data_propiedad).encode("utf-8"))
                print(f"Published message ID: {future.result()}")
                

            else:
                print('No se encontraron datos en el mensaje de Pub/Sub.')
                

        except Exception as e:
            print(f"Error: {e}")
            
            

def manejo_comunicacion():
    project_id = "apps-no-monoliticas-415223"
    subscription_name = "solicitudes_catastro-sub"

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=dar_informacion_catastro_callback)
    print(f"Listening for messages on {subscription_path}...\n")

    # Wrap subscriber in a 'with' block to automatically call close() to close the underlying gRPC channel when done.
    with subscriber:
        try:
            # Blocks the current thread until the subscription is cancelled or an exception is encountered.
            streaming_pull_future.result()
        except TimeoutError:
            streaming_pull_future.cancel()
