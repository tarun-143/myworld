class flight():
	def __init__(self,origin,destination,duration):
		self.ori=origin
		self.dest=destination
		self.dur=duration
	def print_info(self):
		print(f"origin:{self.ori}")
		print(f"destination:{self.dest}")
		print(f"duration:{self.dur}")
	def delay(self,amount):
		self.dur+=amount



def main():
	f1=flight('goa','tokyo',530)
	f1.delay(10)
	f1.print_info()

if __name__ == '__main__':
	main()