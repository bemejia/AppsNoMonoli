from google.cloud import pubsub_v1
from informacion_catastral.modulos.informacion_catastral.aplicacion.servicios import ServicioCatastro

project_id = "apps-no-monoliticas-415223"
subscription_name = "solicitudes_catastro-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)

def dar_informacion_catastro_callback(message):
    try:
        print(f"Received message: {message}")

        sr = ServicioCatastro()
        
        data_message = int(message.data)

        data_propiedad = sr.obtener_informacion_catastral(data_message)

        print(f"Data: {data_propiedad}")
        message.ack()

    except Exception as e:
        print(f"Error: {e}")
        message.ack()


streaming_pull_future = subscriber.subscribe(subscription_path, callback=dar_informacion_catastro_callback)
print(f"Listening for messages on {subscription_path}...\n")

# Wrap subscriber in a 'with' block to automatically call close() to close the underlying gRPC channel when done.
with subscriber:
    try:
        # Blocks the current thread until the subscription is cancelled or an exception is encountered.
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
