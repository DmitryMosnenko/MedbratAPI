#!flask/bin/python3.4

__author__ = 'AMID'

from app import app
app.run(debug=True, threaded=True)