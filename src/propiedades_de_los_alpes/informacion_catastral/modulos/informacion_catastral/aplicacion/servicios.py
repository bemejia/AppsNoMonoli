from propiedades_de_los_alpes.informacion_catastral.modulos.informacion_catastral.infraestructura.fabricas import FabricaInformacionCatastral
from .mapeadores import MapeadorInformacionCatastral

class ServicioCatastro():
    def __init__(self) -> None:
        self._fabrica_informacion_catastral: FabricaInformacionCatastral = FabricaInformacionCatastral()

    @property
    def fabrica_informacion_catastral(self):
        return self.fabrica_informacion_catastral

    def obtener_informacion_catastral(self, id: str):
        mapeador = MapeadorInformacionCatastral()
        return self.fabrica_informacion_catastral.crear_objeto(id, mapeador)
        

