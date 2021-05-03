import logging

import json_log_formatter
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.apm.apm_config import ApmClient

from src.database.migrations import upgrade
from src.settings import DB_URI, HOST, PORT, DEBUG, CELERY, ELASTIC_APM
from src.urls import init_resources


def configure_logs():
    formatter = json_log_formatter.JSONFormatter()
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(formatter)
    LOGGER = logging.getLogger('kiki')
    LOGGER.addHandler(json_handler)
    LOGGER.setLevel(logging.INFO)


def make_app() -> Flask:
    configure_logs()
    flask = Flask(__name__)
    flask.url_map.strict_slashes = False
    flask.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    flask.config['SQLALCHEMY_ECHO'] = True
    flask.config['SQLALCHEMY_BINDS'] = {'default': DB_URI}

    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    flask.config['ELASTIC_APM'] = ELASTIC_APM
    flask.config.update(CELERY)
    upgrade()
    db = SQLAlchemy(flask)
    db.init_app(flask)

    return flask


app = make_app()
init_resources(app)

ApmClient().initialize(ELASTIC_APM)
ApmClient().apm.init_app(app)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
