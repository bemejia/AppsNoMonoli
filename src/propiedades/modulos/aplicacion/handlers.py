from propiedades.seedwork.aplicacion.handlers import Handler
from propiedades.modulos.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedades')