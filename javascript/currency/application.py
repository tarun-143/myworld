import requests

from flask import Flask,jsonify,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')