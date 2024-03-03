from propiedades.seedwork.aplicacion.servicios import Servicio
from propiedades.modulos.dominio.entidades import Propiedad
from propiedades.modulos.dominio.fabricas import FabricaPropiedades
from propiedades.modulos.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.infraestructura.repositorios import RepositorioPropiedades
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

import asyncio

class ServicioPropiedades(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades       
    
    def crear_propeidad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

