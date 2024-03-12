from informacion_propiedades.modulos.dominio.entidades import InformacionPropiedad
from .dto import InformacionPropiedadDTO
from ...config.db import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class RepositorioInformacionPropiedad():

    def crear_propiedad(self, propiedad: InformacionPropiedad):
        propiedaddto = InformacionPropiedadDTO(caracteristica = propiedad.caracteristica,
                                            ciudad = propiedad.ciudad,
                                            id_propiedad = propiedad.id_propiedad,
                                            precio_max = propiedad.precio_max,
                                            precio_min = propiedad.precio_min,
                                            tamano_max = propiedad.tamano_max,
                                            tamano_min = propiedad.tamano_min,
                                            tipo = propiedad.tipo)
        session.add(propiedaddto)
        session.commit()

    def obtener_propiedad(self, id):
        propiedaddto = session.query(InformacionPropiedadDTO).filter_by(id_propiedad=id).first()

        propiedad = InformacionPropiedad()
        propiedad.caracteristica = propiedaddto.caracteristica
        propiedad.ciudad = propiedaddto.ciudad
        propiedad.id_propiedad = propiedaddto.id_propiedad
        propiedad.precio_max = propiedaddto.precio_max
        propiedad.precio_min = propiedaddto.precio_min
        propiedad.tamano_max = propiedaddto.tamano_max
        propiedad.tamano_min = propiedaddto.tamano_min
        propiedad.tipo = propiedaddto.tipo

        return propiedad