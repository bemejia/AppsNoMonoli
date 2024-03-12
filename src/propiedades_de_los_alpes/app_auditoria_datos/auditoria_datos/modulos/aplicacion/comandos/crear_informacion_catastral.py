from auditoria_datos.modulos.infraestructura.repositorio import RepositorioInformacionCatastral
from auditoria_datos.modulos.aplicacion.async_comunication.pulsar_comunication import publicar_mensaje_general, configurar_pulsar
from auditoria_datos.modulos.dominio.entidades import InformacionCatastral


class CrearInformacionCatrastral:
    def __init__(self):
        ...
        

    def iniciar(self, id: int):
        client = configurar_pulsar()
        publicar_mensaje_general(client, "catastro", id)

    def ejecutar(self, informacion_catastral):
        info_catastral = InformacionCatastral(id_propiedad = informacion_catastral.id_propiedad, 
                                              tipo_propiedad= informacion_catastral.tipo_propiedad, 
                                              ubicacion = informacion_catastral.ubicacion,
                                              datos_fiscales = informacion_catastral.datos_fiscales, 
                                              propietario = informacion_catastral.propietario, 
                                              caracteristicas_adicionales = informacion_catastral.caracteristicas_adicionales)
        repo = RepositorioInformacionCatastral()
        repo.agregar_informacion_catastral(info_catastral)

class CompesacionCatastral:
    def __init__(self):
        ...

    def ejecutar(self, id: int = 0):
        print("compensacion de Informacion Catastral")
        client = configurar_pulsar()
        publicar_mensaje_general(client, "catastro", f"compen {id}")

