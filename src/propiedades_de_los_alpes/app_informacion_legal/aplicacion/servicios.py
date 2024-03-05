from propiedades_de_los_alpes.app_informacion_legal.dominio.fabricas import FabricaInfoLegal
from propiedades_de_los_alpes.app_informacion_legal.dominio.repositorios import RepositorioInfoLegal
from propiedades_de_los_alpes.app_informacion_legal.infraestructura.dto import InfoLegal
from propiedades_de_los_alpes.app_informacion_legal.infraestructura.fabricas import FabricaRepositorio
from propiedades_de_los_alpes.app_informacion_legal.infraestructura.mapeadores import MapeadorInfoLegal
from propiedades_de_los_alpes.app_informacion_legal.infraestructura.repositorios import RepositorioInfoLegalPostgres
from seedwork.aplicacion.servicios import Servicio
from .dto import InfoLegalDTO

class ServicioInfoLegal(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_info_legal: FabricaInfoLegal = FabricaInfoLegal()
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_info_legal(self):
        return self._fabrica_info_legal

    def obtener_info_legal(self):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInfoLegalPostgres.__class__)
        info_legal = repositorio.obtener_todos()
        return info_legal
    
    def crear_info_legal(self, info_legal: InfoLegalDTO):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInfoLegalPostgres.__class__)
        map_info =  MapeadorInfoLegal()
        info_legal_entity = map_info.dto_a_entidad(info_legal)
        repositorio.agregar(info_legal_entity)
