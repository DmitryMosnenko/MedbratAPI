__author__ = 'AMID'

from flask import Blueprint, json, jsonify
from app import app, db
from app.models import Cennik
from app.models import Mvc
from app.models import Mv
from app.models import Name
from sqlalchemy.sql import func
from datetime import datetime
import time


mod = Blueprint('checks', __name__, url_prefix='/checks')


# @app.route('/checks/detailed/<date_begin>/<date_end>')
# @app.route('/checks/summary/<date_begin>/<date_end>')
@mod.route('/<detailed>/<date_begin>/<date_end>')
def checks(detailed, date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
        if (detailed != 'detailed') and (detailed != 'summary'):
            raise
    except ValueError:
        return "Unknown date value"
    except:
        return "Unknown required details or no"

    checks = Mvc.query.filter(
        Mvc.datedoc == datetime.now().strftime('%Y-%m-%d'),
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.bodydoc == 1, Mvc.nomwork == 1
    ).all()

    result = {}
    for check in checks:
        result[check.krossnom] = {'id': check.krossnom,
                                  'at': check.datesrok.strftime('%H:%M:%S'),
                                  'checkTotalSum': check.sumcom,
                                  'items': check_detail(check.krossnom, False) if detailed == 'detailed' else ''}

    return json.dumps(result)


@mod.route('/count/<date_begin>/<date_end>')
def checks_count(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.bodydoc == 1, Mvc.nomwork == 1
    ).count()

    return str(result)


@mod.route('/avg/<date_begin>/<date_end>')
def checks_avg(date_begin, date_end):
    try:
        time.strptime(date_begin, '%Y-%m-%d')
        time.strptime(date_end, '%Y-%m-%d')
    except ValueError:
        return "Unknown value"

    result = Mvc.query.with_entities(func.avg(Mvc.sumcom)).filter(
        Mvc.datedoc >= date_begin,
        Mvc.datedoc <= date_end,
        Mvc.tipdoc == 8, Mvc.kodskl == 1, Mvc.bodydoc == 1, Mvc.nomwork == 1
    ).scalar()

    return str(result)


@mod.route('/detail/<id>')
def check_detail(id, to_string=True):
    try:
        id = int(id)
    except ValueError:
        return "Unknown value"

    result = {}

# ToDo: need to try rewrite query using join method, perhaps it will works faster
    details = db.session.query(Name, Mv, Cennik).\
            filter(
                Name.kod == Cennik.namekod,
                Cennik.kod == Mv.kodmat,
                Mv.krossnomer == int(id)
            ).all()

    for detail in details:
        result[detail.Name.name] = {'name': detail.Name.name,
                                    'quantity': float(detail.Mv.kolvo),
                                    'dimension': detail.Cennik.izmerenie,
                                    'retailPrice': float(detail.Mv.cenarasx),
                                    'discount': float(detail.Mv.skidka),
                                    'retailPriceWithoutDiscount': float(detail.Mv.cenaunskidka),
                                    'procurementPrice':
                                        float(detail.Cennik.priceprixod) +
                                        (float(detail.Cennik.priceprixod)/100) *
                                        float(detail.Cennik.procincnds)}

    return json.dumps(result) if to_string else result
