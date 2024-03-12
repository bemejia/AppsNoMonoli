
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    infolegal: typing.List[InfoLegal] = strawberry.field(resolver=obtener_info_legal)