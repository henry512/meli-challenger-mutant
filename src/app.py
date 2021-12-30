from pyms.flask.app import Microservice
from flask_injector import FlaskInjector
from src.containers import container


class App:
    def run(self):
        try:
            ms = Microservice(path=__file__)
            app = ms.create_app()
            FlaskInjector(app=app, modules=[container])
            app.run()
        except Exception:
            exit()
