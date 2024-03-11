from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from auditoria_datos.config.db  import engine

Base = declarative_base()

class InformacionCatastralDto(Base):
    __tablename__ = 'informacion_catastral'
    id_propiedad = Column(Integer, primary_key=True)
    fecha_actualizacion = Column(String)
    tipo_propiedad = Column(String)
    ubicacion = Column(String)
    datos_fiscales = Column(String)
    propietario = Column(String)
    caracteristicas_adicionales = Column(String)
    # Define más campos según necesites

class SagaLogDto(Base):
    __tablename__ = 'saga_log'
    id = Column(String, primary_key=True)
    fecha = Column(String)
    index = Column(Integer)
    comando = Column(String)
    evento_esperado = Column(String)
    error = Column(String)
    compensacion = Column(String)


# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)
