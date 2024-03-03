from propiedades.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "itinerarios"
    odo_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    segmento_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    leg_orden = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False, primary_key=True)
    fecha_llegada = db.Column(db.DateTime, nullable=False, primary_key=True)
    origen_codigo = db.Column(db.String, nullable=False, primary_key=True)
    destino_codigo= db.Column(db.String, nullable=False, primary_key=True)