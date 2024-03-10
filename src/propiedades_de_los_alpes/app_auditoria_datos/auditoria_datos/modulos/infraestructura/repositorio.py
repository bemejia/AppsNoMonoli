from auditoria_datos.modulos.dominio.entidades import InformacionCatastral
from .dto import InformacionCatastralDto
from auditoria_datos.config.db import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

class RepositorioInformacionCatastral():

    def agregar_informacion_catastral(self, informacion_catastral: InformacionCatastral):
        info_catastral = InformacionCatastral(
                        id_propiedad = informacion_catastral.id_propiedad, 
                        fecha_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        tipo_propiedad = informacion_catastral.tipo_propiedad,
                        ubicacion = informacion_catastral.ubicacion,
                        datos_fiscales = informacion_catastral.datos_fiscales,
                        propietario = informacion_catastral.propietario,
                        caracteristicas_adicionales = informacion_catastral.caracteristicas_adicionales
                        )
        session.add(info_catastral)
        session.commit()