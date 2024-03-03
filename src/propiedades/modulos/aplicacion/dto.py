from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.dto import DTO
from typing import List

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    caracteristica: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    id_propiedad: int = field(default_factory=str)
    precio_max: int = field(default_factory=str)
    precio_min: int = field(default_factory=str)
    tamano_max: int = field(default_factory=str)
    tamano_min: int = field(default_factory=str)
    tipo: str = field(default_factory=str)