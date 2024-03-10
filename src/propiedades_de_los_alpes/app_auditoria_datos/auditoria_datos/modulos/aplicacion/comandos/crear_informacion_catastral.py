from auditoria_datos.modulos.infraestructura.repositorio import RepositorioInformacionCatastral

class CrearInformacionCatrastral:
    def __init__(self, repositorio: RepositorioInformacionCatastral):
        self.repositorio = repositorio

    def ejecutar(self, informacion_catastral):
        self.repositorio.agregar_informacion_catastral(informacion_catastral)