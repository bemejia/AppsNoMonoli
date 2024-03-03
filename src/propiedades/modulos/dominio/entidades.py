from __future__ import annotations
from dataclasses import dataclass, field

import propiedades.modulos.dominio.objetos_valor as ov
from propiedades.modulos.dominio.eventos import PropiedadCreada
from propiedades.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Propiedad(AgregacionRaiz):
    caracteristica: ov.Caracteristica = field(default_factory=ov.Caracteristica)
    ciudad: ov.Ciudad = field(default_factory=ov.Ciudad)
    id_propiedad: ov.IdPropiedad = field(default_factory=ov.IdPropiedad)
    precio_max: ov.PrecioMax = field(default_factory=ov.PrecioMax)
    precio_min: ov.PrecioMin = field(default_factory=ov.PrecioMin)
    tamano_max: ov.TamanoMax = field(default_factory=ov.TamanoMax)
    tamano_min: ov.TamanoMin = field(default_factory=ov.TamanoMin)
    tipo: ov.Tipo = field(default_factory=ov.Tipo)

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