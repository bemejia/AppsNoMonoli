from __future__ import annotations
from dataclasses import dataclass, field

from propiedades.modulos.dominio.eventos import PropiedadCreada
from propiedades.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Propiedad(AgregacionRaiz):
    caracteristica: str = field(default=None)
    ciudad: str = field(default=None)
    id_propiedad: int = field(default=None)
    precio_max: int = field(default=None)
    precio_min: int = field(default=None)
    tamano_min: int = field(default=None)
    tamano_max: int = field(default=None)
    tipo: str = field(default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.caracteristica = propiedad.caracteristica
        self.ciudad = propiedad.ciudad
        self.id_propiedad = propiedad.id_propiedad
        self.precio_max = propiedad.precio_max
        self.precio_min = propiedad.precio_min
        self.tamano_max = propiedad.tamano_max
        self.tamano_min = propiedad.tamano_min
        self.tipo = propiedad.tipo

        self.agregar_evento(PropiedadCreada(caracteristica= self.caracteristica, ciudad= self.ciudad, id_propiedad = self.id_propiedad, precio_max= self.precio_max, precio_min= self.precio_min, tamano_max= self.tamano_max, tamano_min= self.tamano_min, tipo= self.tipo))