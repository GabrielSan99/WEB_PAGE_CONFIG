from flask import render_template, request, send_file
from app import app
from flask_qrcode import QRcode




@app.route("/hello_world")
def example():
    return render_template('hello.html')

@app.route("/generate_qr")
def index():
    return render_template("generate_qr_code.html")
