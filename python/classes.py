class point():
	"""docstring for point"""
	def __init__(self, x,y):
		super(point, self).__init__()
		self.x = x
		self.y = y
p=point(input("entr the value"),input("entr the y value"))
print(p.x)
print(p.y)		