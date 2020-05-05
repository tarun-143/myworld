'''this is by using python classes and objects'''
import csv
import os

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:STrrdpsql123@localhost:5432/tarun"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	f=open("flights.csv")
	reeder=csv.reader(f)
	for origin,destination,duration in reeder:
		flight1=flight(origin=origin,destination=destination,duration=duration)
		db.session.add(flight1)
		print(f"added a flight from {origin} to {destination} lasting {duration} minutes ")
	db.session.commit()


if __name__ == '__main__':
	with app.app_context():
		main()