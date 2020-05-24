data={
	'tarun1':'beginner!',
	'varun2':'beginner@',
	'arun3':'beginner#',
	'karun4':'beginner$'
}
admin={
	'admin0':'beginner)'
}
print('\nWelcome to the database Admin program')
usn=input('\nEnter your user name:')
if usn in data.keys():
	pwd=input('\nEnter your password '+usn+':').lower()
	if pwd==data[usn]:
		con=input('\nWould you like to changee your password(y/n):').lower().strip()
		if con=='y':
			new_pass=input('please enter your new password:')
			if len(new_pass)>=8:
				data[usn]=new_pass
			else:
				print('\nyour password has less than 8 characters.your password has not changed!')
		else:
			print('\nok.GoodBye!')
	else:
		print('\nplease verify your password! it is incorrect!')
elif usn in admin.keys():
	pwd=input('\nEnter your password '+usn+':').lower()
	if pwd==admin[usn]:
		print('Here are your data base details:')
		for key,value in data.items():
			print(f'Username : {key}                 password : {value}')
	else:
		print('\nplease verify your password! it is incorrect!')
else:
	print('\nYou have no accont in database.please create an account and come back!')


