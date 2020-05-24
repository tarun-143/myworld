import random
ranges=list(range(1,21))
random=random.choice(ranges)
print('\nWelcome to Guess My Number App')
print('\nyou have 5 guesses to guess my number')
for num in range(1,6):
	guess=int(input(f'\nyour guess {num} : '))
	if guess==random:
		print('congragulations!you won it!')
		break
	if guess>random:
		print('\nyou are too high')
		print(f'you have {5-num} guesses remaining')
	if guess<random:
		print('\nyou are too low')
		print(f'you have {5-num} guesses remaining')
if guess!=random:
	print(f'\nGame Over! My number is {random}.')
	print('Try Again')