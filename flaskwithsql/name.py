import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine("postgresql://postgres:STrrdpsql123@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
	passengers=db.execute("SELECT name,flight_id FROM passengers").fetchall()
	for passenger in passengers:
		print(f"{passenger.name} ")
	nam=str(input("enter the name of the passenger:"))
	passenger=db.execute("SELECT name,flight_id FROM passengers WHERE name=:name",{"name":nam}).fetchone()
	if passenger is None:
		print("error:no such passenger")
		return
	print("Flight_id:")
	print(passenger.flight_id)
	flight=db.execute("SELECT id,origin,destination FROM flights WHERE id=:id",{"id":passenger.flight_id}).fetchone()
	print(f"{flight.origin} to {flight.destination}")
if __name__=="__main__":
	main()