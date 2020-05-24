print('\nWelcome to the even odd number sorter')
while True:
	string=input('Enter the numbers with seperated commas:')
	evens=[]
	odds=[]
	string=string.replace(' ','')
	try:
		string=string.split(',')
		for num in string:
			num=int(num)
		if num%2==0:
			print(f'{num} is even')
			evens.append(num)
		else:
			print(f'{num} is odd ')
			odds.append(num)
		print(f'\nthe following {len(evens)} are the even numbers.')
		for num in evens:
			print('\t-'+str(num))
		print(f'\nthe following {len(odds)} are the odd numbers.')
		for num in odds:
			print('\t-'+str(num))
	except (ValueError):
		print('\nPlease enter numbers with seperated commas!')
	choice=input('\nDo you wnat to run it again(y/n):').lower()
	if choice=='y':
		continue
	else:
		break
print("Thanks for using the program!")


