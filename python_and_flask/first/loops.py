from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	names=["abhi", "tarun", "varun"]
	return render_template("index3.html",names=names)