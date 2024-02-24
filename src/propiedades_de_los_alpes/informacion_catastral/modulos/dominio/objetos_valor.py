from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class id_propiedad():
    id: str

@dataclass(frozen=True)
class tipo_propiedad(Enum):
    Vivienda = "Vivienda"
    Comercial = "Comercial"
    Industrial = "Industrial"
    Terreno = "Terreno"

@dataclass(frozen=True)
class ubicacion():
    pais: str
    departamento: str
    ciudad: str
    direeccion: str
    codigo_postal: str

@dataclass(frozen=True)
class datos_fiscales():
    referencia_catastral: str
    valor_catastral: float
    año_construccion: int
    superficie_terreno: float
    superficie_construida: float

@dataclass(frozen=True)
class propietario():
    nombre: str
    domicilio_fiscal: str

@dataclass(frozen=True)
class CaracteristicasAdicionales():
    tipo_suelo: str
    uso_principal: str
    estado_conservacion: str
    instalaciones: list
    