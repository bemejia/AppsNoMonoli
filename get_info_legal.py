import random
import json
import uuid
import requests
import os
from dotenv import load_dotenv
from propiedades_de_los_alpes.app_informacion_legal.aplicacion.servicios import ServicioInfoLegal
from propiedades_de_los_alpes.app_informacion_legal.infraestructura.mapeadores import MapeadorInfoLegalDTOJson
from propiedades_de_los_alpes.app_informacion_legal.aplicacion.utils.kms import KmsEncryptor
from propiedades_de_los_alpes.app_informacion_legal.pulsar import publicar_mensaje_legal,client
load_dotenv()

def encriptar_info(info):
    kms = KmsEncryptor(os.getenv("KMS_KEY_ID"))
    return kms.encrypt(info)

def run(event, context):
    sr = ServicioInfoLegal()
    info_legal = sr.obtener_info_legal()
    return json.dumps(info_legal)

if __name__ == '__main__':
    print(run(None, None))
