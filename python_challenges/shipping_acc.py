users=['tarun','varun','arun','karun']
print('Welcome to the shipping account login page')
name=input('Enter your username:')
if name in users:
	print(f'Hello {name}.Welcome back to your account.')
	print('currrent shipping costs are:')
	print('\tShipping orders if 1-100:\t10.5INR')
	print('\tShipping orders if 100-500:\t9.5INR')
	print('\tShipping orders if 500-1000:\t7.5INR')
	print('\tShipping orders if over 1000:\t6.5INR')
	orders=int(input('Number of orders you wan to place:'))
	if (orders<100):
		print(f'Total cost of shipping for {orders} orders is {orders*10.5}INR at 10.5INR per order')
	if (orders>100 and orders<500):
		print(f'Total cost of shipping for {orders} orders is {orders*9.5}INR at 9.5INR per order')
	if (orders<1000 and orders>500):
		print(f'Total cost of shipping for {orders} orders is {orders*7.5}INR at 7.5INR per order')
	if (orders>1000):
		print(f'Total cost of shipping for {orders} orders is {orders*6.5}INR at 6.5INR per order')
	con=input('Do u want to continue (y/n):')
	con.lower()
	if con=='y':
		print(f'your {orders} orders will be shipped shortly')
	else:
		print(f'Ok.Hope we will deal next time.Thank You!')

else:
	print(f'Sorry {name}.you do not havean account.')
	print('Please create an account and come back!')