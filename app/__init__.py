__author__ = 'AMID'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models

from app.views import checks
from app.views import static
from app.views import incomes
from app.views import revenue
app.register_blueprint(checks.mod)
app.register_blueprint(static.mod)
app.register_blueprint(incomes.mod)
app.register_blueprint(revenue.mod)