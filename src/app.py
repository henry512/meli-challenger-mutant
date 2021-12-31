from pyms.flask.app import Microservice
from flask_injector import FlaskInjector
from src.containers import container


class App:
    @staticmethod
    def run():
        try:
            ms = Microservice(path=__file__)
            app = ms.create_app()
            FlaskInjector(app=app, modules=[container])
            app.run(host="0.0.0.0")
        except Exception:
            exit()
