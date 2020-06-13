from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("forms.html")

@app.route("/hello", methods=["POST","GET"])
def hello():
	name=request.form.get("nam")
	if request.method=="GET":
		return "please submit the form at default page"
	else:
	    name=name.capitalize()
	    return render_template("submitform.html",name=name)
