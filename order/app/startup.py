import os
import sys
from flask import Flask
from order.api.resource import order
from order.settings import Config
from order.infrastructure.repository.sqlalchemy import dbo


class AppStartup(object):
    def __init__(self, config: Config):
        self._app = Flask(__name__)
        self._app.config.from_object(config)
        dbo.init_app(self._app)
        self._load_router(self._app)

    def _load_router(self, app: Flask):
        app.register_blueprint(order.blueprint)

    @property
    def instance(self):
        return self._app
