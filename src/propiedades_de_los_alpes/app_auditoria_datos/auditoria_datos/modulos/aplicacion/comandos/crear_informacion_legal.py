from auditoria_datos.modulos.infraestructura.repositorio import RepositorioInformacionCatastral
from auditoria_datos.modulos.aplicacion.async_comunication.pulsar_comunication import publicar_mensaje_general, configurar_pulsar
from auditoria_datos.modulos.dominio.entidades import InformacionCatastral
import requests


class CrearInformacionLegal:
    def __init__(self):
        ...
        

    def iniciar(self):
        print("solicitud inciar endpoint")
        url = 'https://ma22f4hfynpb4vh4t2ffdnc6a40kctmf.lambda-url.us-east-1.on.aws'
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print('Solicitud exitosa')


    def ejecutar(self, evento_legal):
        if evento_legal:
            client = configurar_pulsar()
            publicar_mensaje_general(client, "legal", "procesado")
        #info_catastral = evento_legal
        #repo = RepositorioInformacionCatastral()
        #repo.agregar_informacion_catastral(info_catastral)


class CompesacionLegal:
    def __init__(self):
        ...


    def ejecutar(self):
        print("compensacion de Informacion Legal")
        url = "https://u4hcwetfdsnaugsdggt7y77v740rzclz.lambda-url.us-east-1.on.aws"
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print('Solicitud exitosa')

        #info_catastral = evento_legal
        #repo = RepositorioInformacionCatastral()
        #repo.agregar_informacion_catastral(info_catastral)