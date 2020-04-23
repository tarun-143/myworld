from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def default():
	line= "hudhudhuwd"
	return render_template("index.html", line=line)
@app.route("/bye")
def bye():
	line= "goodbye!"
	return render_template("index.html", line=line)
@app.route("/<string:name>")
def hello(name):
	name=name.capitalize()
	line="hello "+name
	return render_template("index.html", line=line)