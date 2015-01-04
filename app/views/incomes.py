__author__ = 'AMID'

from flask import Blueprint, json
from app.models import Mvc
from sqlalchemy.sql import func
import time


mod = Blueprint('incomes', __name__, url_prefix='/incomes')


@mod.route('/<date_begin>/<date_end>')
def incomes(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.with_entities(func.sum(Mvc.sumcom)).filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.bodydoc == 1, Mvc.nomwork == 1
    ).scalar()

    # return str(result)
    return json.dumps(result)