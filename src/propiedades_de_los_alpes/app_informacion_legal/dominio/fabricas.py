from propiedades_de_los_alpes.app_informacion_legal.aplicacion.dto import InfoLegalDTO
from propiedades_de_los_alpes.app_informacion_legal.dominio.entidades import InfoLegal
from seedwork.dominio.repositorios import Mapeador
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaInfoLegal(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        print("Este es el objeto",obj)
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            info_legal: InfoLegal = mapeador.dto_a_entidad(obj)            
            return info_legal

@dataclass
class FabricaInfoLegal(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == InfoLegal.__class__:
            fabrica_info_legal = _FabricaInfoLegal()
            return fabrica_info_legal.crear_objeto(obj, mapeador)
