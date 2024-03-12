class EventoDominio():
    pass

class EventoCatastro(EventoDominio):
    id_propiedad: str
    tipo_propiedad: str
    ubicacion: str
    datos_fiscales: str
    propietario: str
    caracteristicas_adicionales: str

class EventoLegal(EventoDominio):
    ids_creadoas: list[str]

class EventoCatastroFallido(EventoDominio):
    id_propiedad: str
    error: str

class EventoLegalFallido(EventoDominio):
    result: str

    
    