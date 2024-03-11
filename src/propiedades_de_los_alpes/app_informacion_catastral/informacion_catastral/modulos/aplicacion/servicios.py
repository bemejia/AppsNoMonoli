from informacion_catastral.modulos.infraestructura.fabricas import FabricaInformacionCatastral
from .mapeadores import MapeadorInformacionCatastral
from informacion_catastral.modulos.infraestructura.repositorio import RepositorioLogInformacionCatastral
import re

class ServicioCatastro():
    def __init__(self) -> None:
        self._fabrica_informacion_catastral: FabricaInformacionCatastral = FabricaInformacionCatastral()
        self._repositorio_informacion_catastral: RepositorioLogInformacionCatastral = RepositorioLogInformacionCatastral()

    @property
    def fabrica_informacion_catastral(self):
        return self._fabrica_informacion_catastral
    
    @property
    def repositorio_informacion_catastral(self):
        return self._repositorio_informacion_catastral
    
    def compensacion_catastral(self, id: int):
        self.repositorio_informacion_catastral.compensacion_log(id)


    def obtener_informacion_catastral(self, msg: str):
        print("--------------------------------------------------")
        print("Mensaje recibido: ", msg)
        if "compen" in msg:
            id = re.findall(r'\d+', msg)[0]
            self.compensacion_catastral(id)
           

        id = int(msg)
        mapeador = MapeadorInformacionCatastral()
        return self.fabrica_informacion_catastral.crear_objeto(id, mapeador)
        