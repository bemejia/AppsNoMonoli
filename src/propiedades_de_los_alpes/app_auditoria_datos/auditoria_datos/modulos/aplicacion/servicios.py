#from informacion_catastral.modulos.infraestructura.fabricas import FabricaInformacionCatastral
#from .mapeadores import MapeadorInformacionCatastral
from auditoria_datos.modulos.aplicacion.cordinadores.saga import CordinadorAuditoriaDatos
from auditoria_datos.modulos.dominio.eventos import EventoDominio, EventoCatastro
import json

class ServicioMajenoEventos():
    def __init__(self) -> None:
        self._cordinador = CordinadorAuditoriaDatos()
        self._cordinador.iniciar_pasos()
    
    @property
    def cordinador(self):
        return self._cordinador
    
    def majenarevento(self, topico: str, msg: str):
        if topico == "auditoria":
            try:
                id = int(msg)
                
                self.cordinador.iniciar(id)
                
            except ValueError:
                print("El mensaje no esta en el formato correcto")
                return
        elif topico == "catastro":
            try:
                data = json.loads(msg.replace("'", '"'))
                evento = EventoCatastro()
                evento.id_propiedad = data["id_propiedad"]
                evento.tipo_propiedad = data["tipo_propiedad"]
                evento.ubicacion = data["ubicacion"]
                evento.datos_fiscales = data["datos_fiscales"]
                evento.propietario = data["propietario"]
                evento.caracteristicas_adicionales = data["caracteristicas_adicionales"]

            except Exception as e:
                #print(f"Error: {e}")
                return

            self.cordinador.procesar_evento(evento)
                

        

