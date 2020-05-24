print('\nWelcome to yes or no issue voter app')
issue=input('on what isssue you want to conduct poll:')
pwd=input('what is yoour password for poll:')
num=int(input('hoew mnay votes do wannna take:'))
y=0
n=0
results={}
for i in range(1,num+1):
	print(f'\nhere is or issue:{issue}')
	name=input('enter your full name:')
	if name in results.keys():
		print('Sorry!A vote has already been casted in your name')
	else:
		con=input('What is your answer (yes/no):').lower()
		if con=='yes':
			print('Thank you.your answer has been recorded')
			y+=1
		elif con=='no':
			print('Thank you.your answer has been recorded')
			n+=1
		else:
			print('\nyour answer is not in yes or no.Dont worry.still it is noted!')
	results[name]=con
total_votes=len(results.keys())
print(f'\nThe following {total_votes} people casted their votes:')
for key in results:
	print(f'\t-{key}')
print(f'On the following issue:{issue}')
if y>n:
	print(f'Yes Wins! {y} to {n}')
elif n>y:
	print(f'NO Wins! {n} to {y}')
else:
	print(f'The poll is a Tie with {y} votes each!')
rev=input('\nEnter your password to see the poll:')
if rev==pwd:
	for key,value in results.items():
		print(f'name:{name}                    vote:{con} ')
else:
	print('Please check your password!')
print('\nThanks for Using the app!Bye')

