from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.aplicacion.dto import ItinerarioDTO, PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedades.modulos.dominio.entidades import Propiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedades.modulos.aplicacion.mapeadores import MapeadorReserva
from propiedades.modulos.infraestructura.repositorios import RepositorioReservas

@dataclass
class CrearPropiedad(Comando):
    caracteristica : str
    ciudad: str
    id_propiedad: int
    precio_max: int
    precio_min: int
    tamano_max: int
    tamano_min: int
    tipo: int

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                caracteristicas=comando.caracteristicas
            ,   ciudad=comando.ciudad
            ,   id_propiedad=comando.id_propiedad
            ,   precio_max=comando.precio_max
            ,   precio_max=comando.precio_min
            ,   tamano_max=comando.tamano_max
            ,   tamano_min=comando.tamano_min
            ,   tipo=comando.tipo)

        propiedad: Propiedad = self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorReserva())
        propiedad.crear_reserva(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_reserva(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    