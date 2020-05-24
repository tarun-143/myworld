import random
class Pykemon():
	def __init__(self,name,element,speed,health):
		self.name=name.title()
		self.element=element
		self.current_health=health
		self.max_health=health
		self.is_alive=True
		self.speed=speed


	def light_attack(self,enemy_pykemon):
		damage=random.randint(15,25)
		print(f'{self.name} has perfromed {self.moves[0]}')
		print(f'it dealt with a damage of {damage}')
		enemy_pykemon.current_health-=damage


	def heavy_attack(self,enemy_pykemon):
		damage=random.randint(0,50)
		print(f'{self.name} has perfromed {self.moves[1]}')
		if damage<=10:
			print('the attack was missed!')
			print('no damage was dealt')
		else:
			print(f'it dealt with a damage of {damage}')
			enemy_pykemon.current_health-=damage


	def restore(self):
		heal=random.randint(15,25)
		print(f'{self.name} has perfromed {self.moves[2]}')
		self.current_health+=heal
		if self.current_health>self.max_health:
			self.current_health=self.max_health
		print(f'the Pykemon healed by {heal}')


	def faint(self):
		if self.current_health<=0:
			print(f'\n{self.name} has fainted!')
			input('press enetr to continue!\n')
			self.is_alive=False

	def show_stats(self):
		print(f'Name: {self.name}')
		print(f'Element: {self.element}')
		print(f'current health: {self.current_health}')
		print(f'max health : {self.max_health} ')
		print(f'Speed: {self.speed}')

class Fire(Pykemon):
	def __init__(self,name,element,health,speed):
		super().__init__(name,element,health,speed)
		self.moves=['Scratch','Ember','Light','Fireblast']


	def special_attack(self,enemy_pykemon):
		print(f'{self.name} has perfromed {self.moves[3]}')
		if enemy_pykemon.element=='Grass':
			damage=random.randint(35,50)
		elif enemy_pykemon.element=='Water':
			damage=random.randint(5,10)
		else:
			damage=random.randint(10,30)
		print(f'it dealt with a damage of {damage}')
		enemy_pykemon.current_health-=damage


	def move_info(self):
		print('\t MOVES')
		print('-- Scratch --\n An efficient attack...\n Guaranteed to do damage within the range of 15 to 25 damage points.')
		print('-- Ember --\n A risky attack...\n Could deal up to 50 damage points or as little as 0 damage points.')
		print('-- Light --\n A restorative move...\n Guaranteed to heal your Pykemon 15 to 25 health points.')
		print('-- Fire Blast --\n A powerful FIRE based attack...\n Guaranteed to deal MASSIVE damage to GRASS type Pykemon.')


class Water(Pykemon):
	def __init__(self,name,element,health,speed):
		super().__init__(name,element,health,speed)
		self.moves=['Bite','Splash','Dive','Water Cannon']


	def special_attack(self,enemy_pykemon):
		print(f'{self.name} has perfromed {self.moves[3]}')
		if enemy_pykemon.element=='Fire':
			damage=random.randint(35,50)
		elif enemy_pykemon.element=='Grass':
			damage=random.randint(5,10)
		else:
			damage=random.randint(10,30)
		print(f'it dealt with a damage of {damage}')
		enemy_pykemon.current_health-=damage


	def move_info(self):
		print('\t MOVES')
		print('-- Bite --\n An efficient attack...\n Guaranteed to do damage within the range of 15 to 25 damage points.')
		print('-- Splash --\n A risky attack...\n Could deal up to 50 damage points or as little as 0 damage points.')
		print('-- Dive --\n A restorative move...\n Guaranteed to heal your Pykemon 15 to 25 health points')
		print('-- Water Cannon --\n A powerful WATER based attack...\n Guaranteed to deal MASSIVE damage to FIRE type Pykemon.')

class Grass(Pykemon):
	def __init__(self,name,element,health,speed):
		super().__init__(name,element,health,speed)
		self.moves=['Vine Whip','Wrap','Grow','Leaf Blade']

	def special_attack(self,enemy_pykemon):
		print(f'{self.name} has perfromed {self.moves[3]}')
		if enemy_pykemon.element=='Water':
			damage=random.randint(35,50)
		elif enemy_pykemon.element=='Fire':
			damage=random.randint(5,10)
		else:
			damage=random.randint(10,30)
		print(f'it dealt with a damage of {damage}')
		enemy_pykemon.current_health-=damage


	def move_info(self):
		print('\t MOVES')
		print('-- Vine Whip --\n An efficient attack...\n Guaranteed to do damage within the range of 15 to 25 damage points.')
		print('-- Wrap --\n A risky attack...\nCould deal up to 50 damage points or as little as 0 damage points.')
		print('-- Grow --\n A restorative move...\n Guaranteed to heal your Pykemon 15 to 25 health points.')
		print('-- Leaf Blade --\n A powerful GRASS based attack...\n Guaranteed to deal MASSIVE damage to WATER type Pykemon.')

class Game():
	def __init__(self):
		self.elements=['Fire','Water','Grass']
		self.Pykemon_names=['Chewdie', 'Spatol','Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot','Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
		self.battles_won=0


	def create_pykemon(self):
		health=random.randint(70,100)
		speed=random.randint(1,10)
		element=self.elements[random.randint(0,2)]
		name=self.Pykemon_names[random.randint(0,13)]
		if element=='Fire':
			pokemon=Fire(name,element,speed,health)
		elif element=='Water':
			pokemon=Water(name,element,speed,health)
		else:
			pokemon=Grass(name,element,speed,health)
		return pokemon

	def choose_pykemon(self):
		starters=[]
		while len(starters)<3:
			pokemon=self.create_pykemon()
			is_valid=True
			for pokemo in starters:
				if pokemo==pokemon:
					is_valid=False
			if is_valid:
				starters.append(pokemon)
		for pokemon in starters:
			print('\n')
			pokemon.show_stats()
			pokemon.move_info()
			print('\n')
			print('----------------------------------------------------------------------')
		while True:
			print('\nHere are the three pokemon............enter 1 or 2 or 3 to select respective pokemon')
			choice=input('What is your choice : ')
			if choice=='1':
				return starters[0]
				break
			elif choice=='2':
				return starters[1]
				break
			elif choice=='3':
				return starters[2]
				break
			else:
				print('\nit is an invalid option')


	def get_attack(self,pykemon):
		count=1
		print('\nyour pykemom moves:\n')
		for move in pykemon.moves:
			print(f'{count}.{move}')
			count+=1
		while True:
			choice=input('What is your move : ')
			if choice=='1' or choice=='2' or choice=='3' or choice=='4':
				break
			else:
				print('it is an invalid move!!')
		return choice


	def player_attack(self,choice,player,computer):
		print('\n')
		if choice=='1':
			player.light_attack(computer)
		elif choice=='2':
			player.heavy_attack(computer)
		elif choice=='3':
			player.restore()
		elif choice=='4':
			player.special_attack(computer)
		computer.faint()

	def computer_attack(self,player,computer):
		print('\n')
		choice=str(random.randint(1,4))
		if choice=='1':
			computer.light_attack(player)
		elif choice=='2':
			computer.heavy_attack(player)
		elif choice=='3':
			computer.restore()
		elif choice=='4':
			computer.special_attack(player)
		player.faint()

	def battle(self,player,computer):
		move=self.get_attack(player)
		if player.speed>=computer.speed:
			self.player_attack(move,player,computer)
			if computer.is_alive:
				self.computer_attack(player,computer)
		else:
			self.computer_attack(player,computer)
			if player.is_alive:
				self.player_attack(move,player,computer)



print('\nWelcome to the pykemon Game')
while True:
	game=Game()
	print('Choose one of the Three pokemon')
	player_pokemon=game.choose_pykemon()
	print('\n')
	print('---'+player_pokemon.name+'---')
	player_pokemon.show_stats()
	input('\n press enter to continue\n')
	round=1
	while player_pokemon.is_alive:
		print(f'------------------# Round{round}#----------------')
		computer_pokemon=game.create_pykemon()
		print('enemy_pykemon : \n')
		print('---'+computer_pokemon.name+'---')
		computer_pokemon.show_stats()
		while player_pokemon.is_alive and computer_pokemon.is_alive:
			game.battle(player_pokemon,computer_pokemon)
			if player_pokemon.is_alive and computer_pokemon.is_alive:
				print('\n')
				print('Your Pykemon:  ')
				player_pokemon.show_stats()
				print('\n')
				print('Enemy Pykemon: ')
				computer_pokemon.show_stats()
				print('-----------------------------------------------------------')
		if player_pokemon.is_alive:
			game.battles_won+=1
			round+=1
	print(f'\n{player_pokemon.name} has won {game.battles_won} battles!')
	choice=input('\nDo u want to play again(y/n) : ').lower()
	if choice=='n':
		break
print('Thanks for playing the game!!!!have a good day!')










































