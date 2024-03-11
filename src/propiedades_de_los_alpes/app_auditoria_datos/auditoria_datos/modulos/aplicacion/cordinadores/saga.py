from dataclasses import dataclass
import uuid
import datetime
from abc import ABC, abstractmethod
from auditoria_datos.modulos.infraestructura.repositorio import RepositorioSagaLog
from auditoria_datos.modulos.dominio.eventos import EventoDominio, EventoCatastro, EventoCatastroFallido
from auditoria_datos.modulos.aplicacion.comandos.crear_informacion_catastral import  CrearInformacionCatrastral


class Paso():
    id_correlacion: str
    fecha_evento: datetime.datetime
    index: int
    def __init__(self):
        self.fecha_evento = datetime.datetime.now()
        self.id_correlacion = uuid.uuid4()

class Inicio(Paso):
    index: int

    def __init__(self):
        super().__init__()
        self.index = 0

class Fin(Paso):
    def __init__(self, index):
        super().__init__()
        self.index = index


class Transaccion(Paso): 
    id_correlacion: str 
    fecha_evento: datetime.datetime
    comando: any
    evento: EventoDominio
    error: EventoDominio
    compensacion: any
    exitosa: bool

    def __init__(self, index, comando, evento, error, compensacion):
        super().__init__()
        self.index = index
        self.comando = comando
        self.evento = evento
        self.error = error
        self.compensacion = compensacion

class CoordinadorOrquestacion(ABC):
    pasos: list[Paso]
    index: int
    
    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
                
    def es_ultima_transaccion(self, index):
        if index == len(self.pasos) - 1:
            return True
        else:
            return False
    
    def persistir_en_saga_log(self, paso):
        ...
    
    def procesar_evento(self, evento: EventoDominio):
        ...




class CordinadorAuditoriaDatos(CoordinadorOrquestacion):
    def iniciar_pasos(self):
        self.pasos = [
            Inicio(),
            Transaccion(index=1, comando = CrearInformacionCatrastral, evento=EventoCatastro, error=EventoCatastroFallido, compensacion=None),
            #Transaccion(index=2, comando=, evento=, error=, compensacion=),
            #Transaccion(index=2, comando=, evento=, error=, compensacion=),
            Fin(index=3)
        ]

    def iniciar(self, id: int):
        print("Saga Inicada")
        self.persistir_en_saga_log(self.pasos[0])
        self.pasos[1].comando.iniciar(self, id)
        


    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, paso):
        repositorio = RepositorioSagaLog()
        if isinstance(paso, Inicio) or  isinstance(paso, Fin):
            transaccion = Transaccion(paso.index, None, None, None, None)
            repositorio.agregar_saga_log(transaccion)
        
        elif isinstance(paso, Transaccion):
            transaccion = Transaccion(paso.index, paso.comando, paso.evento, paso.error, paso.compensacion)
            repositorio.agregar_saga_log(transaccion)

    def procesar_evento(self, evento: EventoDominio):#, #evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):
            self.terminar()
        elif isinstance(evento, paso.evento):
            self.pasos[index].comando.ejecutar(self, evento)
            self.persistir_en_saga_log(self.pasos[index])
            if index + 1 < len(self.pasos)-1:
                self.pasos[index+1].comando.iniciar()
            else:
                self.terminar()

        elif isinstance(evento, paso.error):
            self.pasos[index].compensacion.ejecutar(self, evento)
            self.persistir_en_saga_log(self.pasos[index])
            if index - 1 > 0:
                self.pasos[index-1].compensacion.inciar()





        
