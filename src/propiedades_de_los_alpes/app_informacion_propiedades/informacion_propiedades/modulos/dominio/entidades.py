""" Entidades del dominio de la información catastral."""

from dataclasses import dataclass, field

@dataclass
class InformacionPropiedad():
    caracteristica: str = field(default=None)
    ciudad: str = field(default=None)
    id_propiedad: int = field(default=None)
    precio_max: int = field(default=None)
    precio_min: int = field(default=None)
    tamano_max: int = field(default=None)
    tamano_min: int = field(default=None)
    tipo: str = field(default=None)

    def __str__(self) -> str:
        return str({"caracteristica": self.caracteristica,
                "ciudad": self.ciudad,
                "id_propiedad": self.id_propiedad,
                "precio_max": self.precio_max,
                "precio_min": self.precio_min,
                "tamano_max": self.tamano_max,
                "tamano_min": self.tamano_min,
                "tipo": self.tipo})