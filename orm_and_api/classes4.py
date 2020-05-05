class flight:
	counter=1
	def __init__(self,origin,destination,duration):
		self.id=flight.counter
		flight.counter+=1
		self.passengers=[]


		self.ori=origin
		self.dest=destination
		self.dur=duration


	def print_info(self):
		print(f"origin:{self.ori}")
		print(f"destination:{self.dest}")
		print(f"duration:{self.dur}")
		print("\n")
		print("passengers")


		for passenger in self.passengers:
			print(f"{passenger.name}")

	def add_passenger(self,p):
		self.passengers.append(p)
		p.flight_id=self.id


	def delay(self,amount):
		sef.duration+=amount


class passenger:
	def __init__(self,name):
		self.name=name



def main():

	f1=flight('goa','denmark',330)
	alice=passenger('Alice')
	bob=passenger('Bob')
	f1.add_passenger(alice)
	f1.add_passenger(bob)
	f1.print_info()
if __name__ == '__main__':
	main()
	