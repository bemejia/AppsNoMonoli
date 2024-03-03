from propiedades.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    caracteristica = db.Column(db.String, primary_key=True, nullable=False)
    ciudad = db.Column(db.String, primary_key=True, nullable=False)
    id_propiedad = db.Column(db.Integer, primary_key=True, nullable=False)
    precio_max = db.Column(db.Integer, primary_key=True, nullable=False)
    precio_min = db.Column(db.Integer, nullable=False, primary_key=True)
    tamano_max = db.Column(db.Integer, nullable=False, primary_key=True)
    tamano_min = db.Column(db.Integer, nullable=False, primary_key=True)
    tipo= db.Column(db.String, nullable=False, primary_key=True)
