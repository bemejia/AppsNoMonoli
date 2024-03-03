from propiedades.seedwork.aplicacion.queries import Query, QueryResultado
from propiedades.seedwork.aplicacion.queries import ejecutar_query as query
from propiedades.modulos.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from propiedades.modulos.aplicacion.mapeadores import MapeadorPropiedad

@dataclass
class ObtenerPropiedad(Query):
    id: str

class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedad =  self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=propiedad)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)