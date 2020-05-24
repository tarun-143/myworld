print('Welcome to the factor generator app')
num=int(input('Enter the number:'))
i=1
factors=[]
print(f'The factors of {num} are:')
while(i!=num+1):
	if num%i==0:
		print(i)
		factors.append(i)
	i+=1
print("Summary:")
for i in factors:
	print(f'{i} * {int(num/i)} = {num} ')
choice=input('\nDo u want to run it again(y/n):').lower()
while(True):
	if choice=='y':
		num=int(input('Enter the number:'))
		factors=[]
		i=1
		while(i!=num+1):
			if num%i==0:
				print(i)
				factors.append(i)
			i+=1
		print("Summary:")
		for i in factors:
			print(f'{i} * {int(num/i)} = {num} ')
		choice=input('\nDo u want to run it again(y/n):')
	else:
		break
print('\nThanks for using the program')

