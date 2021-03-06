from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__, instance_relative_config=False)
    
    _secret_key = []
    random_key = os.urandom(16)
    _secret_key.append(random_key)

    app.config.from_mapping(
        SECRET_KEY = _secret_key[0],
        SQLALCHEMY_DATABASE_URI = "sqlite:///instance/database/location.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS = False,)
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    @app.route("/hello")
    def hello():
        _hello = """Hello friend, How are you?"""
        return render_template("base.html", _hello=_hello)
    
    from . import client
    app.register_blueprint(client.client_bp)
    
    from . import auto
    app.register_blueprint(auto.auto_bp)
    
    return app
