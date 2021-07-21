from flask import (
  Blueprint,
  render_template,
  url_for,
  request,
  redirect,
  flash
  )
from .models import db, Auto

auto_bp = Blueprint("auto", __name__)

@auto_bp.route("/auto")
def auto():
    return render_template("auto.html")
    
@auto_bp.route("/add_auto", methods=["POST", "GET"])
def add_auto():
    if request.method == "POST":
      
        error = None

        nombre = request.form["nombre"]
        modelo = request.form["modelo"]
        ano = request.form["año"]
        pais = request.form["país"]
        
        if not nombre:
            error = "Nombre no puede estar vacío."
        elif not modelo:
            error = "Modelo no puede estar vacío."
        if error is not None:
            flash(error)
        else:
            autos = Auto(
                      nombre=nombre,
                      modelo=modelo,
                      ano=ano,
                      pais=pais
          )
            db.session.add(autos)
            db.session.commit()
        
            message = "¡Datos agregados satisfactoriamente!"
            flash(message)
        
            return redirect(url_for("auto.show_auto"))
    return render_template("auto.html")
   
@auto_bp.route("/show_auto")
def show_auto():
    autos_ = Auto.query.all()
    return render_template("show_auto.html", autos_=autos_)