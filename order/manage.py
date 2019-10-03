import os
import sys
import click
import loadpkg
from click import Choice, Group
from plugin.server.gunicorn import FlaskGunicorn, WorkerMode
from order.app import application
from order.settings import config


@click.command()
@click.option("--port", "-p", "port", default=config.SERVER_PORT, type=int, help="Gunicorn running port")
@click.option("--worker", "-w", "worker", default=4, type=int, help="Gunicorn worker process number")
@click.option("--mode", "-k", "mode",
              type=Choice(WorkerMode.list()),
              default=WorkerMode.SYNC,
              help="Gunicorn worker mode")
def gunicorn(port, worker, mode):
    """Run production server provided by Gunicorn"""
    FlaskGunicorn(application.instance).run()


@click.command()
@click.option("--port", "-p", "port", default=config.SERVER_PORT, type=int, help="Server running port")
def server(port):
    """Run development server provided by Flask"""
    application.instance.run(host="0.0.0.0", port=port, threaded=True)


if __name__ == "__main__":
    commands = Group(context_settings={"help_option_names": ['-h', '--help']})
    commands.add_command(server, "serve")
    commands.add_command(gunicorn, "gunicorn")
    commands()
