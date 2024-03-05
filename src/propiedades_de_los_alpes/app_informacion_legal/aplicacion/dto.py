from dataclasses import dataclass
from seedwork.aplicacion.dto import DTO

@dataclass()
class InfoLegalDTO(DTO):
    fecha_creacion: str
    id: str
    tipo_propiedad: str
    pais: str
    departamento: str
    ciudad: str
    direccion: str
    estado_legal: str
    tipo_contrato: str
    documento_legal: str
    valor_catastral: int
    anio_construccion: int
    superficie_terreno: int
    superficie_construida: int
    nombre_propietario: str
    domicilio_propietario: str
    uuid: str

