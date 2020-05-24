import random
print("Let's play Rock Paper Scissors Game")
options=['Rock','Paper','Scissors']
comp=random.choice(options)
p=0
c=0
rounds=int(input('How many rounds do u like to play:'))
for i in range(1,rounds+1):
	print('Round '+str(i))
	print(f'player:{p}            computer:{c}')
	pick=input('Time to pick Rock,Paper,Scissors.......:')
	print(f'\tcomputer:{comp}')
	print(f'\tplayer:{pick.title()}')
	if pick.title()  not in options:
		print('\tinvalid option')
		print('\tcomputer won')
		c+=1
	if comp==pick.title():
		print('\tIt is a Tie')
	if (comp=='Scissors' and pick.title()=='Paper'):
		print('\tcomputer won')
		print(f'\t{comp} cuts {pick.title()}')
		c+=1
	if (comp=='Scissors' and pick.title()=='Rock'):
		print('\tplayer won')
		print(f'\t{comp} broken by {pick.title()}')
		p+=1
	if (comp=='Paper' and pick.title()=='Rock'):
		print('\tcomputer won')
		print(f'\t{comp} folds {pick.title()}')
		c+=1
	if (comp=='Paper' and pick.title()=='Scissors'):
		print('\tplayer won')
		print(f'\t{comp} cut by {pick.title()}')
		p+=1
	if (comp=='Rock' and pick.title()=='Paper'):
		print('\tplayer won')
		print(f'\t{comp} folded by {pick.title()}')
		p+=1
	if (comp=='Rock' and pick.title()=='Scissors'):
		print('\tcomputer won')
		print(f'\t{comp} broke {pick.title()}')
		c+=1
print('Game Results:')
print(f'\tcomputer:{c}')
print(f'\tplayer:{p}')

if p>c:
	print(f'\tplayer Won finally with a lead of {p-c}!')
if c>p:
	print(f'\tcomputer Won finally with a lead of {c-p}!')
if c==p:
	print(f'\tWhat a Game.It is a Tie')