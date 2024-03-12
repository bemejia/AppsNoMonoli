#from informacion_catastral.modulos.infraestructura.fabricas import FabricaInformacionCatastral
#from .mapeadores import MapeadorInformacionCatastral
from auditoria_datos.modulos.aplicacion.cordinadores.saga import CordinadorAuditoriaDatos
from auditoria_datos.modulos.dominio.eventos import EventoDominio, EventoCatastro, EventoLegal, EventoLegalFallido
import json
import ast
import traceback


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

                self.cordinador.procesar_evento(evento)

            except Exception as e:
                #print(f"Error: {e}")
                return
        elif topico == "legal":
            try:
                data =  ast.literal_eval(msg)

                if "result"  in data:
                    evento_error  = EventoLegalFallido()
                    evento_error.result = data["result"]
                    self.cordinador.procesar_evento(evento_error)
                    return
                print("datos legal:", data, "tipo:", type(data))
                evento = EventoLegal()
                evento.ids_creadoas = data
                self.cordinador.procesar_evento(evento)

            except Exception as e:
                print(f"Error: {e}")
                # Esto captura la excepción y extrae información sobre la misma
                exc_type, exc_value, exc_traceback = traceback.sys.exc_info()
                #Extraemos el nombre del archivo y el número de línea
                filename, line_number, _, _ = traceback.extract_tb(exc_traceback)[-1]
                print(f"Se ha producido un error en el archivo '{filename}', en la línea {line_number}.")
                return

            
                

        

