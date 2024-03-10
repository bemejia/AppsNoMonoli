from dataclasses import dataclass
import uuid
import datetime
from abc import ABC, abstractmethod


class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int

@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    ...
class CoordinadorOrquestacion(ABC):
    pasos: list[Paso]
    index: int
    
    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
                
    def es_ultima_transaccion(self, index):
        return len(self.pasos) - 1

    def procesar_evento(self):#, #evento: EventoDominio):
        ...
        #paso, index = self.obtener_paso_dado_un_evento(evento)
        #if es_ultima_transaccion(index) and not isinstance(evento, paso.error):
        #    self.terminar()
        #elif isinstance(evento, paso.error):
        #    self.publicar_comando(evento, self.pasos[index-1].compensacion)
        #elif isinstance(evento, paso.evento):
        #    self.publicar_comando(evento, self.pasos[index+1].compensacion)





class Transaccion:
    def __init__(self, index, comando, evento, error, compensacion):
        self.index = index
        self.comando = comando
        self.evento = evento
        self.error = error
        self.compensacion = compensacion





class CordinadorAuditoriaDatos:

    def inciar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearReserva, evento=ReservaCreada, error=CreacionReservaFallida, compensacion=CancelarReserva),
            #Transaccion(index=2, comando=, evento=, error=, compensacion=),
            #Transaccion(index=2, comando=, evento=, error=, compensacion=),
            Fin(index=3)
        ]


    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def finalizar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, paso):
        pass
