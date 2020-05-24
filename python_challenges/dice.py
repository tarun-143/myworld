import random
def dice(sides):
	list_of_numbers=range(1,sides+1)
	choice=list_of_numbers[random.randint(1,sides)]
	return choice
print('\nWelcome to the dice roller')
while True:
	sides=int(input('\nHow many sides do u want to create a dice with:'))
	rolls=int(input('How many times do u want to roll:'))
	print(f'\nyou rolled {rolls} {sides} sided rolls')
	print('\n-------------the results are here---------------')
	outputs=[]
	for i in range(1,rolls+1):
		output=dice(sides)
		outputs.append(output)
	for out in outputs:
		print(out)
	print(f'your total score is : {sum(outputs)}')
	choice=input('\ndo u want to roll it again(y/n):').lower()
	if choice=='n':
		break
print('\nThanks for using the dice roller!')

