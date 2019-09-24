import multiprocessing
from flask import Flask
from gunicorn.app.base import Application, BaseApplication


class WorkerMode(object):
    SYNC = "sync"
    EVENTLET = "eventlet"
    GREENLET = "greenlet"
    GREVENT = "grevent"

    @classmethod
    def list(cls):
        return [
            cls.SYNC, cls.EVENTLET, cls.GREENLET, cls.GREVENT
        ]


class FlaskGunicorn(BaseApplication):

    def __init__(self, app: Flask, host="0.0.0.0", port="8000", workers=4, mode=WorkerMode.SYNC):
        self.options = {
            "bind": f"{host}:{port}",
            "workers": workers,
            "worker_class": mode
        }
        self._application = app
        super(FlaskGunicorn, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self._application
