

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.migrations import upgrade
from src.settings import DB_URI, HOST, PORT, DEBUG, CELERY, ELASTIC_APM
from src.urls import set_urls

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
set_urls(app)
app.config['ELASTIC_APM'] = ELASTIC_APM
app.config.update(CELERY)
db = SQLAlchemy(app)
upgrade()


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
