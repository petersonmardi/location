from flask import (
  Blueprint,
  render_template,
  url_for,
  redirect,
  )

auto_bp = Blueprint("auto", __name__)
@auto_bp.route("/auto")
def auto():
    return render_template("auto.html")
    

@auto_bp.route("/agregar")
def add():
    return "<h1>Agrégame</h1>"
    
@auto_bp.route("/editar")
def edit():
    return "<h1>Edítame</h1>"
    
@auto_bp.route("/eliminar")
def delete():
    return "<h1>Elimíname</h1>"