def printname(names):
	for name in names:
		if name=='tarun':
			print(name)
			return 'hi'
	for name in names:
		if name=='rahul':
			print(name)
			return 'hi2'


names=['tarun','rahul']
result=printname(names)
print(result)