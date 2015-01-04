__author__ = 'AMID'

from flask import Blueprint, json, jsonify
from app import app, db
from app.models import Cennik
from app.models import Mvc
from app.models import Mv
from app.models import Name
import time


mod = Blueprint('revenue', __name__, url_prefix='/revenue')


@mod.route('/<date_begin>/<date_end>')
def net_profit(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    checks = Mvc.query.filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.bodydoc == 1, Mvc.nomwork == 1
    ).all()

    result = 0

    for check in checks:
        details = db.session.query(Name, Mv, Cennik).\
            filter(
                Name.kod == Cennik.namekod,
                Cennik.kod == Mv.kodmat,
                Mv.krossnomer == check.krossnom
            ).all()
        for detail in details:
            result += (float(detail.Mv.cenarasx) * float(detail.Mv.kolvo)) - ((float(detail.Cennik.priceprixod) + ((float(detail.Cennik.priceprixod)/100) * float(detail.Cennik.procincnds))) * float(detail.Mv.kolvo))

    return str(result)

