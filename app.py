from email import message
from sre_parse import State
from xml.sax import default_parser_list
from flask import Flask, render_template, request
import os, subprocess

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action') == 'Save Settings':
            ssid = request.form.get('ssid')
            password = request.form.get('password')
            print("Your SSID is " + ssid + " and your password is " + password)
            os.system('nmcli dev wifi connect '+ ssid +' password '+ password)
            #nmcli dev wifi connect SSID-Name password wireless-password

        else:
            pass
    elif request.method == 'GET':
        
        return render_template('index.html')
    
    return render_template('index.html')





a = subprocess.run(['nmcli','dev'], check=True, stdout=subprocess.PIPE).stdout
stdout = subprocess.run(['nmcli', 'dev'], check=True, capture_output=True, text=True).stdout
data = [1,2,3];
state = 'off'

@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            os.system('nmcli r wifi ' + state)
        elif  request.form.get('action2') == 'VALUE2': 
            os.system('nmcli r wifi on')
        elif  request.form.get('action3') == 'VALUE3': 
            password = request.form.get('password')
            ssid = request.form.get('ssid')
            print(password, ssid)
        else:
            pass # unknown
    elif request.method == 'GET':
        
        return render_template('test.html', data=data)
    
    return render_template("test.html")