# -*- coding: cp1251 -*-
__author__ = 'AMID'

from app import app, db
from .models import Cennik
from .models import Mvc
from .models import Mv
from .models import Name
from sqlalchemy.sql import func
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    cennik1 = Cennik.query.first()
    return "Hello, World! -- " + cennik1.name

@app.route('/about')
def about():
    return __author__

@app.route('/today')
def today():
    checks = Mvc.query.filter_by(
        datedoc=datetime.now().strftime('%Y-%m-%d'),
        # datedoc='2014-08-08',
        tipdoc=8,
        kodskl=1,
        bodydoc=1,
        nomwork=1
    ).all()

    strResult = "<b>Total sum: {} ({}) uah - {} checks</b> <br>".format(
        round(
            Mvc.query.with_entities(func.sum(Mvc.sumcom)).filter_by(
                    datedoc=datetime.now().strftime('%Y-%m-%d'),
                    # datedoc='2014-08-08',
                    tipdoc=8,
                    kodskl=1,
                    bodydoc=1,
                    nomwork=1
                ).scalar(),
            2
        ),
        round(
            # Purchasing sum without NDS
            Mvc.query.with_entities(func.sum(Mvc.sumskl)).filter_by(
                    datedoc=datetime.now().strftime('%Y-%m-%d'),
                    # datedoc='2014-08-08',
                    tipdoc=8,
                    kodskl=1,
                    bodydoc=1,
                    nomwork=1
                ).scalar(),
            2
        ),
        # round(
        #     # Selling NDS sum
        #     Mvc.query.with_entities(func.sum(Mvc.sumnds)).filter_by(
        #             datedoc=datetime.now().strftime('%Y-%m-%d'),
        #             tipdoc=8,
        #             kodskl=1,
        #             bodydoc=1,
        #             nomwork=1
        #         ).scalar(),
        #     2
        # ),
        len(checks)
    )

    profit = 0

    for check in checks:
        strResult += "{} - <b> {} uah</b><br>".format(check.datesrok, round(check.sumcom, 2))

        details = db.session.query(Name, Mv, Cennik).\
            filter(
                Name.kod == Cennik.namekod,
                Cennik.kod == Mv.kodmat,
                Mv.krossnomer == check.krossnom
            ).all()
        for detail in details:
            strResult += "--- {} -- {} {} * {} ({}) {} {}<br>".format(
                detail.Name.name,
                detail.Mv.kolvo,
                detail.Cennik.izmerenie,
                detail.Mv.cenarasx,  # the selling price (including discount)
                detail.Mv.cenaprix,  # the purchase price
                '-' + str(detail.Mv.skidka) + '%' if detail.Mv.skidka and detail.Mv.skidka > 0 else '',
                '(' + str(detail.Mv.cenaunskidka) + ')' if detail.Mv.skidka and detail.Mv.skidka > 0 else ''  # the selling price (without discount)
            )
            profit += ((detail.Mv.cenarasx - detail.Mv.cenaprix) * detail.Mv.kolvo)

        # break

    strResult += "<b>{}</b>".format(profit)

    return strResult