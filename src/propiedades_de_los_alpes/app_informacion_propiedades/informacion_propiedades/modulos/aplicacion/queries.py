from informacion_propiedades.modulos.infraestructura.repositorio import RepositorioInformacionPropiedad

def ejecutar_query(id:int):
    repositorio = RepositorioInformacionPropiedad()
    return repositorio.obtener_propiedad(id)