__author__ = 'AMID'

import os


if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'firebird+fdb://sysdba:masterkey@127.0.0.1:3050/D:/Medbrat/BASEDATA.FDB?charset=win1251'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['MAPI_DATABASE_URL']


# SQLALCHEMY_DATABASE_URI = 'firebird+fdb://sysdba:masterkey@192.168.51.181:3050/C:/BASEDATA.FDB?charset=win1251'