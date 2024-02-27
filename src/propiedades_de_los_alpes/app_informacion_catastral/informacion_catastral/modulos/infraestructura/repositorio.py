from informacion_catastral.modulos.dominio.entidades import InformacionCatastral
from .dto import LogInformacionCatastral
from informacion_catastral.config.db import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

class RepositorioLogInformacionCatastral():

    def agregar_log(self, informacion_catastral: InformacionCatastral):
        log = LogInformacionCatastral(id_propiedad=informacion_catastral.id_propiedad, 
                                      fecha_consulta= datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                      fecha_entrega= datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        session.add(log)
        session.commit()