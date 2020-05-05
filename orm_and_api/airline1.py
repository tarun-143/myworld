import os

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:STrrdpsql123@localhost:5432/tarun"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
	flights=flight.query.all()
	return render_template("airline0.html",flights=flights)
@app.route("/book",methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    Flight=flight.query.get(flight_id)
    if Flight is None:
        return render_template('error.html')
    Passenger=passenger(name=name,flight_id=flight_id)
    db.session.add(Passenger)
    db.session.commit()
    return render_template("success.html")




@app.route("/flights")
def flights():
    flights=flight.query.all() 
    return render_template("list.html",flights=flights)




@app.route("/flights/<int:flight_id>")
def details(flight_id):
    Flight=flight.query.get(flight_id)
    if Flight is None:
        return render_template('error.html')


    passengers=passenger.query.filter_by(flight_id=flight_id)
    return render_template('details.html',flight=flight,passengers=passengers)

