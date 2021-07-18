from flask import (
  Blueprint,
  render_template,
  url_for,
  redirect,
  request,
  flash
  )

from .models import db, Clients

client_bp = Blueprint("client", __name__)

@client_bp.route("/client")
def client():
    return render_template("client.html")
    

@client_bp.route("/agregar_clientes", methods=["POST", "GET"])
def add_clients():
    if request.method == "POST":
      
        error = None
        message = None
        
        name = request.form["name"]
        passport = request.form["passport"]
        cedula = request.form["cedula"]
        telephone = request.form["telephone"]
        hours = request.form["hours"]
        days = request.form["days"]
        price = request.form["price"]
        
        if not name:
            error = "Espacio es requerido."
        elif not telephone:
            error = "Espacio es requerido."
        elif not hours:
            error = "Espacio es requerido."
        elif not days:
            error = "Espacio es requerido."
        elif not price:
            error = "Espacio es requerido."
        
        if error is not None:
            flash(error)
        else:
            clients = Clients(
                      id=None,
                      name=name,
                      passport=passport,
                      cedula=cedula,
                      telephone=telephone,
                      hours=hours,
                      days=days,
                      price=price,
                      rent=None
                      )
            db.session.add(clients)
            db.session.commit()
            
            message = "¡Datos agregados satisfactoriamente!"
            
            flash(message)
            return redirect(url_for("client.client"))
    return render_template("client.html")
    
@client_bp.route("/editar")
def edit():
    return "<h1>Edítame</h1>"
    
@client_bp.route("/eliminar")
def delete():
    return "<h1>Elimíname</h1>"