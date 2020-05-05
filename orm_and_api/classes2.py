class flight():
	def __init__(self,origin,destination,duration):
		self.ori=origin
		self.dest=destination
		self.dur=duration
	def print_info(self):
		print(f"origin:{self.ori}")
		print(f"destination:{self.dest}")
		print(f"duration:{self.dur}")


def main():
	f1=flight('goa','paris',500)
	print("Flight 1:")
	f1.print_info()
	print("\n")

	f2=flight('goa','london',550)
	print("Flight 2:")
	f2.print_info()
if __name__ == '__main__':
	main()