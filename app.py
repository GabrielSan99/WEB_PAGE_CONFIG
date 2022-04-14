from email import message
from xml.sax import default_parser_list
from flask import Flask, render_template, request
import os, subprocess

app = Flask(__name__)

data = [1,2,3]

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            os.system('nmcli r wifi off')
        elif  request.form.get('action2') == 'VALUE2':
            os.system('nmcli r wifi on')
        else:
            pass # unknown
    elif request.method == 'GET':
        
        return render_template('index.html', 
        message='zis')
    
    return render_template("index.html", )