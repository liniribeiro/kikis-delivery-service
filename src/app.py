

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.apm.apm_config import ApmClient
from src.migrations import upgrade
from src.settings import DB_URI, HOST, PORT, DEBUG, CELERY, ELASTIC_APM
from src.urls import set_urls

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
set_urls(app)
app.config['ELASTIC_APM'] = ELASTIC_APM
app.config.update(CELERY)
db = SQLAlchemy(app)
db.init_app(app)

ApmClient().initialize(ELASTIC_APM)
ApmClient().apm.init_app(app)



if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
