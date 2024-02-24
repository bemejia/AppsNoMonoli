from dataclasses import dataclass
from propiedades_de_los_alpes.seekwork.dominio.fabricas import Fabrica
from propiedades_de_los_alpes.informacion_catastral.modulos.dominio.entidades import InformacionCatastral

@dataclass
class FabricaInformacionCatastral(Fabrica):
        def crear_objeto(self, id: int, mapeador: any = None) -> InformacionCatastral:
            return mapeador.obtener_informacion_catastral(id)

        