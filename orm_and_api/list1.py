import os

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:STrrdpsql123@localhost:5432/tarun"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	flights=flight.query.all()
	for fligh in flights:
		print(f"{fligh.origin} to {fligh.destination} in {fligh.duration} minutes")

	f3=flight.query.get(3)
	f3.duration=290
	db.session.commit()


if __name__ == '__main__':
	with app.app_context():
		main()