import random
class Creature():
	def __init__(self,name):
		self.name=name.title()
		self.boredom=0
		self.hunger=0
		self.dirtness=0
		self.tiredness=0
		self.is_alive=True
		self.is_awake=True
		self.food=2

	def eat(self):
		if self.food>0:
			self.hunger-=random.randint(1,4)
			self.food-=1
			print(f'Yum!{self.name} has a great meal!')
		else:
			print('There is no sufficient food in inventory! Better go for forage!')
		if self.hunger<0:
			self.hunger=0
	def play(self):
		print(f'\n{self.name} wants to play a game ')
		value=random.randint(0,2)
		print(f'{self.name} was thinking of a number in 0,1,2 ')
		guess=int(input('What is your guess:'))
		if guess==value:
			self.boredom-=3
			print('\nYour guess was correct')
		else:
			self.boredom-=1
			print('Wrong guess!')
		if self.boredom<0:
			self.boredom=0
	def sleep(self):
		self.is_awake=False
		self.tiredness-=3
		self.boredom-=1
		if self.boredom<0:
			self.boredom=0
		if self.tiredness<0:
			self.tiredness=0
	def awake(self):
		value=random.randint(0,2)
		if value==0:
			print(f'{self.name} is just wokeup!')
			self.is_awake=True
			self.tiredness=0
		else:
			print(f'{self.name} is still sleeping......Zzzzzzzzzzzzzz ')
			self.sleep()
	def clean(self):
		self.dirtness=0
		print(f'{self.name} has just took a bath it is total clean!')
	def forage(self):
		self.dirtness+=2
		food_found=random.randint(0,4)
		self.food+=food_found
		print(f'\n{self.name} has found {food_found} peices of food')
	def show_values(self):
		print(f'\nCreature name : {self.name}')
		print(f'hunger : {self.hunger} ')
		print(f'tiredness : {self.tiredness} ')
		print(f'dirtness : {self.dirtness} ')
		print(f'boredom : {self.boredom} ')
		print(f'\ncurrent food inventory : {self.food} peices')
		if self.is_awake:
			print('current status : awake')
		else:
			print('current status : sleeping')
	def increments(self,difficulty):
		self.hunger+=random.randint(0,difficulty)
		self.dirtness+=random.randint(0,difficulty)
		if self.is_awake:
			self.tiredness+=random.randint(0,difficulty)
			self.boredom+=random.randint(0,difficulty)
	def kill(self):
		if self.hunger>=10:
			print(f'{self.name} has died due to hunger! ')
			self.is_alive=False
		elif self.dirtness>=10:
			print(f'{self.name} has died due to infection!')
			self.is_alive=False
		elif self.boredom>=10:
			self.boredom=10
			print(f'{self.name} is feelin bored and falling asleep!')
			self.is_awake=False
		elif self.tiredness>=10:
			print(f'{self.name} if feeeling tired and falling asleep!')
			self.is_awake=False




def showmenu(creature):
	if creature.is_awake:
		print('\nEnter 1 to eat')
		print('Enter 2 to play')
		print('Enter 3 to bath')
		print('Enter 4 to sleep')
		print('Enter 5 to forage for food')
		choice=(input('\nEnter your choice : '))
		return choice
	else:
		choice=(input('\nEnter 6 to try awake thw creature! : '))
		choice='6'
		return choice

def call_function(creature,choice):
	if choice=='1':
		creature.eat()
	elif choice=='2':
		creature.play()
	elif choice=='3':
		creature.clean()
	elif choice=='4':
		creature.sleep()
	elif choice=='5':
		creature.forage()
	elif choice=='6':
		creature.awake()
	else:
		print('Sorry that is an invalid option!')



print('\nWelcome to the Pythaogachi simulator app')
difficulty=int(input('enter your difficulty level : '))
if difficulty>5:
	difficulty=5
if difficulty<1:
	difficulty=1



while True:
	name_of_creature=input('\nEnter the name of your creature : ')
	creature=Creature(name_of_creature)
	rounds=1
	while creature.is_alive:
		print(f'\n---------------#Round{rounds}---------------')
		creature.show_values()
		choice=showmenu(creature)
		call_function(creature,choice)
		creature.increments(difficulty)
		creature.kill()
		rounds+=1
		input('press enter to continue')
	print('\nR.I.P')
	print(f'{creature.name} has survived for {rounds-1} rounds ')
	opt=input('Do u want to play again(Y/N) : ').lower()
	if opt=='n':
		break
print('Thanks for palying the game!:-)')


	