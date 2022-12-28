from flask import Flask
import logging
from flask_toastr import Toastr
from .database import init_db

f = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
logging.basicConfig(filename="log.log", filemode="a", format=f, level=logging.DEBUG)

toastr = Toastr()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "a_secret_key"
    app.config["TOASTR_POSITION_CLASS"] = "toast-top-center"
    app.config["TOASTR_OPACITY"] = False
    with app.app_context():
        db = init_db()
        toastr.init_app(app)
        from . import routes
        return app
