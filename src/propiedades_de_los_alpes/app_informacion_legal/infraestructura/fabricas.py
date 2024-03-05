from dataclasses import dataclass, field

from propiedades_de_los_alpes.app_informacion_legal.aplicacion.dto import InfoLegalDTO
from seedwork.dominio.repositorios import Repositorio
from .repositorios import RepositorioInfoLegalPostgres
from .excepciones import ExcepcionFabrica
from seedwork.dominio.fabricas import Fabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioInfoLegalPostgres.__class__:
            return RepositorioInfoLegalPostgres()
        else:
            raise ExcepcionFabrica()
        
        