class EventoDominio():
    pass

class EventoCatastro(EventoDominio):
    id_propiedad: str
    tipo_propiedad: str
    ubicacion: str
    datos_fiscales: str
    propietario: str
    caracteristicas_adicionales: str

class EventoCatastroFallido(EventoDominio):
    id_propiedad: str
    error: str

    
    