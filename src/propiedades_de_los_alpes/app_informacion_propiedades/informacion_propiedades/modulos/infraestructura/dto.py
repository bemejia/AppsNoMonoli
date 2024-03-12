from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from ...config.db import engine

Base = declarative_base()

class InformacionPropiedadDTO(Base):
    __tablename__ = 'informacion_propiedad'

    id_propiedad = Column(Integer, primary_key=True, autoincrement=True)
    caracteristica = Column(String)
    ciudad = Column(String)
    precio_max = Column(Integer)
    precio_min = Column(Integer)
    tamano_max = Column(Integer)
    tamano_min = Column(Integer)
    tipo = Column(String)

Base.metadata.create_all(engine)