from __future__ import annotations
from dataclasses import dataclass
from propiedades.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadCreada(EventoDominio):
    caracteristica: str = None
    ciudad: str = None
    precio_max: int = None
    precio_min: int = None
    tamano_max: int = None
    tamano_min: int = None
    tipo: str = None