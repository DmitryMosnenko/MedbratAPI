__author__ = 'AMID'

from flask import Blueprint, json
from app.models import Mvc, Mv
from sqlalchemy.sql import func
import time


mod = Blueprint('incomes', __name__, url_prefix='/incomes')


@mod.route('/<date_begin>/<date_end>')
def incomes_total(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.with_entities(func.sum(Mvc.sumcom)).filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.nomwork == 1
    ).scalar()

    return json.dumps(result)


@mod.route('/cash/<date_begin>/<date_end>')
def incomes_cash(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.with_entities(func.sum(Mvc.sumcom)).filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipsaledoc == 0,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.nomwork == 1
    ).scalar()

    return json.dumps(result)


@mod.route('/terminal/<date_begin>/<date_end>')
def incomes_terminal(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.with_entities(func.sum(Mvc.sumcom)).filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipsaledoc == 1,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.nomwork == 1
    ).scalar()

    return json.dumps(result)


@mod.route('/rebate/<date_begin>/<date_end>')
def incomes_rebate(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mv.query.with_entities(func.sum(Mv.kolvo * Mv.cenaunskidka - Mv.kolvo * Mv.cenarasx)).filter(
        Mv.datadoc >= date_begin,
        Mv.datadoc <= date_end,
        Mv.tipdoc == 8, Mv.kodsklada == 1
    ).scalar()

    return json.dumps(float(result))
