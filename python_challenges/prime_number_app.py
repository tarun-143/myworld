import time
print('Welcome to the Prime Number App')
while True:
	print('Eneter 1 to determine Wheather anumber is prme or not')
	print('Eneter 2 to see primes in arange of numbers')
	choice=input('Eneter 1 or 2:')
	if choice=='1':
		num=int(input('Enter the number:'))
		i=2
		factors=[]
		while i!=num:
			if num%i==0:
				factors.append(i)
				break
		if len(factors)==0:
			print(f'{num} is prime!')
		else:
			print(f'{num} is non prime! ')
	elif choice=='2':
		low=int(input('Enetr the lower range integer:'))
		high=int(input('Enetr the hoigher range integer:'))
		primes=[]
		start=time.time()
		for num in range(low,high+1):
			prime_status=True
			for i in range(2,num):
				if num%i==0:
					prime_status=False
					break
			if prime_status:
				primes.append(num)
			else:
				continue
		end=time.time()
		print(f'calclated in {round((end-start),4)} seconds...............')
		input('press enter to see the list')
		for num in primes:
			print(num)
	else:
		print('please enter 1 or 2!Try again!')
	choice=input('\nDo you wnat to run it again(y/n):').lower()
	if choice=='y':
		continue
	else:
		break
print("Thanks for using the program!")




		
			
