import informacion_catastral.async_comunication.informacion_catastral as app
import os

def ejecutar_app(event, context):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./informacion_catastral/async_comunication/private_key_pub_sub.json"
    app.dar_informacion_catastro_callback(event)
    return '204'
