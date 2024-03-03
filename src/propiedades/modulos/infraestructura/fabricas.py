from dataclasses import dataclass, field
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.repositorios import Repositorio
from propiedades.modulos.dominio.repositorios import RepositorioProveedores, RepositorioReservas
from .repositorios import RepositorioReservasSQLite, RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas.__class__:
            return RepositorioReservasSQLite()
        elif obj == RepositorioProveedores.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()