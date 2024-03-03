from dataclasses import dataclass, field
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.repositorios import Repositorio
from propiedades.modulos.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()