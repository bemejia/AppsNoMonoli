from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from informacion_catastral.config.db import engine

Base = declarative_base()

class LogInformacionCatastral(Base):
    __tablename__ = 'log_informacion_catastral'
    id_log = Column(Integer, primary_key=True, autoincrement=True)
    id_propiedad = Column(Integer)
    fecha_consulta = Column(String)
    fecha_entrega = Column(String)
    
    # Define más campos según necesites

# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)