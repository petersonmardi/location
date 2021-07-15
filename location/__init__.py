from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__, instance_relative_config=False)

    db.init_app(app)

    _secret_key = []
    random_key = os.urandom(16)
    _secret_key.append(random_key)

    app.config.from_mapping(
        SECRET_KEY = _secret_key[0],
        SQLALCHEMY_DATABASE_URI = "sqlite:///database.db",
        SQLALCHEMY_TRACK_MODIFICATIONS = True,
    )

    with app.app_context():
        db.create_all()

    @app.route("/hello")
    def hello():
        hello_ = """Hello friend, How are you?"""
        return render_template("base.html", hello_=hello_)
    
    from . import auto
    app.register_blueprint(auto.auto_bp)
    
    from . import client
    app.register_blueprint(client.client_bp)
    
    from . import index
    app.register_blueprint(index.index_bp)

    return app
