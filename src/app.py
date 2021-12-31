from pyms.flask.app import Microservice
from flask_injector import FlaskInjector
from src.containers import container
from flask_script import Manager, Server
from flask_cors import CORS


class App:
    @staticmethod
    def run():
        try:
            ms = Microservice(path=__file__)
            app = ms.create_app()
            FlaskInjector(app=app, modules=[container])
            CORS(app)
            manager = Manager(app)
            manager.add_command("runserver", Server(host="0.0.0.0", port="5000", threaded=True))
            manager.run()
        except Exception:
            exit()
