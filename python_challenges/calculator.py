def addition(num_1,num_2):
	sume=round(num_1+num_2,3)
	print(f'\nThe sum of {num_1} and {num_2} is {sume}')
	result=f'{num_1}+{num_2}={sume}'
	print(result)
	return result
def sub(num_1,num_2):
	dif=round(num_1-num_2,3)
	print(f'\nThe difference of {num_1} and {num_2} is {dif}')
	result=f'{num_1}-{num_2}={dif}'
	print(result)
	return result
def mul(num_1,num_2):
	pro=round(num_1*num_2,3)
	print(f'\nThe product of {num_1} and {num_2} is {pro}')
	result=f'{num_1}*{num_2}={pro}'
	print(result)
	return result
def div(num_1,num_2):
	try:
		div=round(num_1/num_2,3)
		print(f'\nThe divisoin of {num_1} and {num_2} is {div}')
		result=f'{num_1}/{num_2}={div}'
		print(result)
		return result
	except ZeroDivisionError:
		print('\ndivision with zero is not possible!')
def exp(num_1,num_2):
	exp=round(num_1**num_2,3)
	print(f'\nthe result of {num_1} raised to the power of {num_2} is {exp}')
	result=f'{num_1}**{num_2}={exp}'
	print(result)
	return result
history=[]
print('\nWelcome to the python calculator')
while True:
	num_1=float(input('\nEnter a number:'))
	num_2=float(input('Enter the other number:'))
	operator=input('Enter the operator addition,subtraction,division,multiplication or exponentiation:').lower()
	if operator=='addition' or operator=='a':
		result=addition(num_1,num_2)
		history.append(result)
	elif operator=='subtraction' or operator=='s':
		result=sub(num_1,num_2)
		history.append(result)
	elif operator=='multiplication' or operator=='m':
		result=mul(num_1,num_2)
		history.append(result)
	elif operator=='division' or operator=='d':
		result=div(num_1,num_2)
		history.append(result)
	elif operator=='exponentiation' or operator=='e':
		result=exp(num_1,num_2)
		history.append(result)
	else:
		print('Enter a valid operator')
	choice=input('\ndo u want to run it again(y/n):').lower()
	if choice=='y':
		continue
	elif choice=='n':
		print('\nSummary----------')
		for i in history:
			print(i)
		break
print('\nThank you for using the calculator!')