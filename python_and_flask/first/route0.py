from flask import Flask, render_template 
 
app = Flask(__name__)
 
@app.route("/")
def default():
 	return "hello wrld"

@app.route("/<string:name>")
def hello(name):
 	return f"hello {name}!"
