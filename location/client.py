from flask import (
  Blueprint,
  render_template,
  url_for,
  request,
  redirect,
  flash
  )
from .models import *

client_bp = Blueprint("client", __name__)

@client_bp.route("/")
def client():
    return render_template("client.html")
    
@client_bp.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
      
        error = None
        message = None

        nombre = request.form["nombre"]
        cedula = request.form["cédula"]
        pasaporte = request.form["pasaporte"]
        telefono = request.form["teléfono"]
        
        if not nombre:
            error = "Nombre no puede estar vacío."
        elif not telefono:
            error = "Teléfono no puede estar vacío."
        if error is not None:
            flash(error)
        else:
            clients = Client(
                      nombre=nombre,
                      cedula=cedula,
                      pasaporte=pasaporte,
                      telefono=telefono
          )
            db.session.add(clients)
            db.session.commit()
        
            message = "¡Datos agregados satisfactoriamente!"
            
        flash(message)
        
        return redirect(url_for("client.show"))
    return render_template("client.html")
   
@client_bp.route("/show")
def show():
    clients_ = Client.query.all()
    return render_template("show.html", clients_=clients_)