from flask import Flask
from order.api.resource import order
from order.settings import Config


class AppStartup(object):
    def __init__(self, config: Config):
        self._app = Flask(__name__)
        self._app.config.from_object(config)
        self._load_router(self._app)

    def _load_router(self, app: Flask):
        app.register_blueprint(order.blueprint)

    @property
    def instance(self):
        return self._app
