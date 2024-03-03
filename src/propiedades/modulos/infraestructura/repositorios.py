from propiedades.config.db import db
from propiedades.modulos.dominio.repositorios import RepositorioPropiedades
from propiedades.modulos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedades.modulos.dominio.entidades import Propiedad
from propiedades.modulos.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_vuelos.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)