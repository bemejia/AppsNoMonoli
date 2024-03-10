from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from auditoria_datos.config.db  import engine

Base = declarative_base()

class InformacionCatastralDto(Base):
    __tablename__ = 'informacion_catastral'
    id_propiedad = Column(Integer)
    fecha_actualizacion = Column(String)
    tipo_propiedad = Column(String)
    ubicacion = Column(String)
    datos_fiscales = Column(String)
    propietario = Column(String)
    caracteristicas_adicionales = Column(String)
    # Define más campos según necesites

# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)