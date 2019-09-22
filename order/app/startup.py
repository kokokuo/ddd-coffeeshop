from flask import Flask
from flask_restful import Api
from orders.settings import BaseConfig


class AppStartup(object):
    def __init__(self, config: BaseConfig):
        self._app = Flask(__name__)
        self._app.config.from_object(config)
        self._routing(self._app)

    def _routing(self, app: Flask):
        pass

    @property
    def app(self):
        return self._app
