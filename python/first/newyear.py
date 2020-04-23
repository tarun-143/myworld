import datetime

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
	now=datetime.datetime.now()
	newyear= now.month==1 and now.day==1
	return render_template("index2.html", newyear=newyear)