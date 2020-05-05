class flight():
	def __init__(self,origin,destination,duration):
		self.ori=origin
		self.dest=destination
		self.dur=duration
def main():

	f=flight('moscow',"hyderabad",530)

	f.dur+=10

	print(f.ori)
	print(f.dest)
	print(f.dur)

if __name__=="__main__":
	main()