from auditoria_datos.modulos.dominio.entidades import InformacionCatastral
from .dto import InformacionCatastralDto
from auditoria_datos.config.db import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .dto import SagaLogDto

Session = sessionmaker(bind=engine)
session = Session()

class RepositorioInformacionCatastral():

    def agregar_informacion_catastral(self, informacion_catastral: InformacionCatastral):
        registro_existente = session.query(InformacionCatastralDto).filter_by(id_propiedad=informacion_catastral.id_propiedad).first()
        if registro_existente:
            registro_existente.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            registro_existente.tipo_propiedad = str(informacion_catastral.tipo_propiedad)
            registro_existente.ubicacion = str(informacion_catastral.ubicacion)
            registro_existente.datos_fiscales = str(informacion_catastral.datos_fiscales)
            registro_existente.propietario = str(informacion_catastral.propietario)
            registro_existente.caracteristicas_adicionales = str(informacion_catastral.caracteristicas_adicionales)
            session.commit()
            return
        else:
            info_catastral = InformacionCatastralDto(
                            id_propiedad = informacion_catastral.id_propiedad, 
                            fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            tipo_propiedad = str(informacion_catastral.tipo_propiedad),
                            ubicacion = str(informacion_catastral.ubicacion),
                            datos_fiscales = str(informacion_catastral.datos_fiscales),
                            propietario = str(informacion_catastral.propietario),
                            caracteristicas_adicionales = str(informacion_catastral.caracteristicas_adicionales)
                            )
            session.add(info_catastral)
            session.commit()

class RepositorioSagaLog():
    def agregar_saga_log(self, transaccion):
        saga_log = SagaLogDto(
            id = transaccion.id_correlacion,
            fecha = str(transaccion.fecha_evento),
            index = transaccion.index,
            comando = str(transaccion.comando),
            evento_esperado = str(transaccion.evento),
            error = str(transaccion.error),
            compensacion = str(transaccion.compensacion)
        )
        session.add(saga_log)
        session.commit()