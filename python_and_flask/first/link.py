from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("firstpage.html")
@app.route("/full")
def more():
	return render_template("more.html")
	