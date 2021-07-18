from . import db
from datetime import datetime as dt

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(13), nullable=True)
    passport = db.Column(db.String(9), nullable=True)
    telephone = db.Column(db.Integer, nullable=False)
    hours = db.Column(db.String(10), nullable=True)
    days = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.DateTime, nullable=False, default=dt.now)

    def __repr__(self):
        return f"{self.name} is the author."


class Autos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    _model = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.name} is the author."

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.name} is the author."

