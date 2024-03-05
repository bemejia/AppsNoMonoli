"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""
from sqlalchemy import create_engine

from propiedades_de_los_alpes.app_informacion_legal.config.db import Database
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
db = Database()
session = db.Session()
Base = declarative_base()


class InfoLegal(Base):
    __tablename__ = 'info_legal'
    id = Column(Integer, primary_key=True)
    fecha_creacion = Column(String)
    tipo_propiedad = Column(String)
    pais = Column(String)
    departamento = Column(String)
    ciudad = Column(String)
    direccion = Column(String)
    estado_legal = Column(String)
    tipo_contrato = Column(String)
    documento_legal = Column(String)
    valor_catastral = Column(Integer)
    anio_construccion = Column(Integer)
    superficie_terreno = Column(Integer)
    superficie_construida = Column(Integer)
    nombre_propietario = Column(String)
    domicilio_propietario = Column(String)
    uuid = Column(String)

engine = db.get_engine()
Base.metadata.create_all(engine)