from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Caracteristica():
    nombre: str

@dataclass(frozen=True)
class Ciudad():
    nombre: str

@dataclass(frozen=True)
class IdPropiedad():
    nombre: int

@dataclass(frozen=True)
class PrecioMax():
    nombre: int

@dataclass(frozen=True)
class PrecioMin():
    nombre: int

@dataclass(frozen=True)
class TamanoMax():
    nombre: int

@dataclass(frozen=True)
class TamanoMin():
    nombre: int

@dataclass(frozen=True)
class Tipo():
    nombre: str