from flask import Flask
from flask_script import Manager
from flask_qrcode import QRcode


app = Flask(__name__)
app.config.from_object('config')    #apply the configurations of the file config.py

manager = Manager(app)
qrcode = QRcode(app)

from app.controllers import default