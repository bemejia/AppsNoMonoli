""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""
from propiedades_de_los_alpes.app_informacion_legal.config.db import Database
from propiedades_de_los_alpes.app_informacion_legal.dominio.repositorios import RepositorioInfoLegal
from .dto import InfoLegal
from .mapeadores import MapeadorInfoLegal
from uuid import UUID
from propiedades_de_los_alpes.app_informacion_legal.dominio.fabricas import FabricaInfoLegal

class RepositorioInfoLegalPostgres(RepositorioInfoLegal):

    def __init__(self):
         self.db = Database()
         self._fabrica_info_legal: FabricaInfoLegal = FabricaInfoLegal()


    def agregar(self, info_legal: InfoLegal):
        session = self.db.get_session()
        session.add(info_legal)
        session.commit()

    def actualizar(self, entity: InfoLegal):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_por_id(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_todos(self):
        session = self.db.get_session()
        entries = session.query(InfoLegal).all()
        print(entries)