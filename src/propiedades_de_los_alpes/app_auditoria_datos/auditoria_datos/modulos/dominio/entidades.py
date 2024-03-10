""" Entidades del dominio de la información catastral."""

from dataclasses import dataclass, field
from . import objetos_valor as ov

@dataclass
class InformacionCatastral():
    id_propiedad: ov.id_propiedad = field(default_factory=ov.id_propiedad)
    tipo_propiedad: ov.tipo_propiedad = field(default_factory=ov.tipo_propiedad)
    ubicacion: ov.ubicacion = field(default_factory=ov.ubicacion)
    datos_fiscales : ov.datos_fiscales = field(default_factory=ov.datos_fiscales)
    propietario: ov.propietario = field(default_factory=ov.propietario)
    caracteristicas_adicionales: ov.CaracteristicasAdicionales = field(default_factory=ov.CaracteristicasAdicionales)

    def __str__(self) -> str:
        return str({"id_propiedad": self.id_propiedad,
                "tipo_propiedad": self.tipo_propiedad,
                "ubicacion": self.ubicacion,
                "datos_fiscales": self.datos_fiscales,
                "propietario": self.propietario,
                "caracteristicas_adicionales": self.caracteristicas_adicionales})