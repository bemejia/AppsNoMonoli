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

def get_run(event, context):
    sr = ServicioInfoLegal()
    info_legal = sr.obtener_info_legal()
    return json.dumps(info_legal)

def comp_run(event, context):
    sr = ServicioInfoLegal()
    info_legal = sr.borrar_ultimos_ids()
    return {
        "statusCode": 200,
        "body": "Deleted last ids"
    }

def run(event, context):
    info_legal = requests.get(os.getenv("INFO_LEGAL_URL"))
    sr = ServicioInfoLegal()
    ids = []
    for info in info_legal.json():
        info["uuid"] = str(uuid.uuid4())
        info["domicilio_propietario"] = encriptar_info(info["domicilio_propietario"])
        map_info =  MapeadorInfoLegalDTOJson()
        info_legal_dto = map_info.externo_a_dto(info)
        id_info_legal = sr.crear_info_legal(info_legal_dto)
        ids.append(info["uuid"])
    print("Los ids agregados son: ", ids)
    opciones = ['{"result":"Error en el microservicio."}', ids]
    respuesta = random.choice(opciones)
    publicar_mensaje_legal(client, respuesta)
    response = {
        "statusCode": 200
    }
    return response

if __name__ == '__main__':
    print(run(None, None))
