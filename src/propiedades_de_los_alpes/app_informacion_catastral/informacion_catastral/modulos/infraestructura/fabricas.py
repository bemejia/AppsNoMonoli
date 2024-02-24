from dataclasses import dataclass
from informacion_catastral.modulos.dominio.entidades import InformacionCatastral

@dataclass
class FabricaInformacionCatastral():
        def crear_objeto(self, id: int, mapeador: any = None) -> InformacionCatastral:
            return mapeador.obtener_informacion_catastral(id)

        