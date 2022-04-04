from flask import render_template, jsonify
from app import app


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")


@app.route("/scan")
def scanner_qr():
    return render_template("scan.html")

@app.route('/get_config')
def get_config():
  api_key = 123456
  username = 'admin'
  password = 'admin'
  config = {'Configs':{'Api_key': api_key, 'Ap_username': username, 'Ap_password': password}}
  return jsonify(config)  #api needs json format in return





@app.route("/hello_world")
def hello_world():
    return render_template('hello.html')

@app.route("/generate_qr")
def generate_qr():
    return render_template("generate_qr_code.html")

# @app.route("/webcam")
# def open_web_cam():
#     return render_template("webcam.html")


@app.route("/file_save_test")
def open_web_cam():
    return render_template("file_save_test.html")





