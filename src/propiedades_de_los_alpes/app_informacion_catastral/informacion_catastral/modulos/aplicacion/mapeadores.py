import requests
from informacion_catastral.modulos.dominio.entidades import InformacionCatastral
from informacion_catastral.modulos.infraestructura.repositorio import RepositorioLogInformacionCatastral
from datetime import datetime

# Definir el endpoint
url = 'https://servicio-tercero-catastro-3ttobfplwa-uc.a.run.app/propiedad/'

class MapeadorInformacionCatastral:
    def acl_info_catastral(self, informacion_as_is):
        datos  = informacion_as_is
        ubicacion = {"pais": datos["pais"],
                        "ciudad": datos["ciudad"], 
                        "departamento": datos["departamento"], 
                        "direccion": datos["direccion"], 
                        "codigo_postal": datos["codigo_postal"]}
        datos_fiscales = {"referencia_catastral": datos["referencia_catastral"],
                            "valor_catastral": datos["valor_catastral"],
                            "año_construccion": datos["año_construccion"],
                            "superficie_terreno": datos["superficie_terreno"],
                            "superficie_construida": datos["superficie_construida"]}
        propietario = {"nombre_propietario": datos["nombre"],
                        "domicilio_fiscal": datos["domicilio_fiscal"]}
        caracteristicas_adicionales = {"tipo_suelo": datos["tipo_suelo"],
                                        "uso_principal": datos["uso_principal"],
                                        "estado_conservacion": datos["estado_conservacion"],
                                        "instalaciones": datos["instalaciones"]}
        return InformacionCatastral(
            id_propiedad = datos['id_propiedad'],
            tipo_propiedad = datos['tipo_propiedad'],
            ubicacion = ubicacion,
            datos_fiscales = datos_fiscales,
            propietario = propietario,
            caracteristicas_adicionales = caracteristicas_adicionales
        )

    def obtener_informacion_catastral(self, id: str) -> InformacionCatastral:
        respuesta = requests.get(url + str(id))
        if respuesta.status_code == 200:
            # Convertir el archivo JSON de resultado en un diccionario de Python
            datos = respuesta.json()
            informacion_catastral = self.acl_info_catastral(datos)
            # Crear un objeto de la clase InformacionCatastral
            repositorio_log = RepositorioLogInformacionCatastral()
            repositorio_log.agregar_log(informacion_catastral)
                              
            return informacion_catastral
            
        else:
            print(f'Error en la solicitud: {respuesta.status_code}')

