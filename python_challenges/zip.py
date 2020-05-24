names=['dhoni','virat','ashwin','sachin']
jerseys=[7,18,99,10]

for name,jersey in zip(names,jerseys):
	print(name.title()+':'+str(jersey))

