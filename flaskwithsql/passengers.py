import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine("postgresql://postgres:STrrdpsql123@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights=db.execute("SELECT id,origin,destination,duration FROM flights").fetchall()
	for flight in flights:
		print(f"{ flight.id }:{ flight.origin } to { flight.destination } in { flight.duration } minutes")

	flight_id= int(input("\nFlight ID: "))
	flight=db.execute("SELECT origin,destination,duration FROM flights WHERE id=:id",{"id":flight_id}).fetchone()

	if flight is None:
		print("error:No such flight")
		return
	passengers=db.execute("SELECT name FROM passengers WHERE flight_id=:id",{"id":flight_id}).fetchall()
	print("\npassengers:")
	for passenger in passengers:
		print(passenger.name)
	if len(passengers)==0:
		print('No passengers')
    
if __name__=="__main__":
	main()