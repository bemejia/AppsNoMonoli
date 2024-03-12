import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def consultar_catastro(self, id_catastro: str, info: Info) -> CatrastoRespuesta:
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, str(id_catastro).encode(), "persistent://nomonoliticas/default/catastro", "public/default/catastro")
        return CatrastoRespuesta(mensaje="Procesando Mensaje de Catastro", codigo=203)