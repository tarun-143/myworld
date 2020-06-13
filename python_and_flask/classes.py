class point():
	"""docstring for point"""
	def __init__(self, x,y):
		super(point, self).__init__()
		self.u = x
		self.v = y
p=point(input("entr the value"),input("entr the y value"))
print(p.u)
print(p.v)		