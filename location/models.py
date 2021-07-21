from . import db
from datetime import datetime as dt

class Client(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    
    nombre = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(20), nullable=True)
    pasaporte = db.Column(db.String(9), nullable=True)
    telefono = db.Column(db.Integer, nullable=False)
    
    fecha = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return f"{self.name} is the author."


class Auto(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    pais = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return f"{self.name} is the author."

class ClientAuto(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    auto_id = db.Column(db.Integer, db.ForeignKey('auto.id_'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id_'), nullable=False)

    def __repr__(self):
        return f"<Auto_id>: {self.auto_id}."

