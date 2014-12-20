# -*- coding: cp1251 -*-
__author__ = 'AMID'

from app import app, db
from .models import Cennik
from .models import Mvc

@app.route('/')
@app.route('/index')
def index():
    cennik1 = Cennik.query.first()
    # print(str(cennik1.__dict__))
    # return str(cennik1.__dict__).replace("'","\"")
    return "Hello, World! -- " + cennik1.name

@app.route('/about')
def about():
    return __author__

@app.route('/today')
def today():
    checks = Mvc.query.filter_by(datedoc='2014-12-20').all()
    # print(checks.__dict__)
    return str(checks[10].datesrok)
    # return checks.sumcom
