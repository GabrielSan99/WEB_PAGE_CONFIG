from flask import render_template, request, send_file
from app import app
from flask_qrcode import QRcode

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")


@app.route("/scan")
def scanner_qr():
    return render_template("scan.html")





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





