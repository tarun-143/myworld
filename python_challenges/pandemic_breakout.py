import random
class Simulation():
	def __init__(self):
		self.day_number=1
		self.population_size=int(input('\nEnter the population_size of the city : '))
		self.infection_size=int(input('\nEnter the initial infected percentage : '))
		self.infected_percent=self.infection_size/100
		self.probability_of_infection=int(input('\nwhat is the probability of infecion when exposed to a disese : '))
		self.infection_durarion=int(input('\nEnter the duration of the infecion : '))
		self.mortality_rate=int(input('\nWhat is the mortality rate of the infrcted persons : '))
		self.sim_days=int(input('\nWhat are the Simulation days : '))


class Person():
	def __init__(self):
		self.is_alive=True
		self.is_infected=False
		self.days_infected=0


	def infect(self,simulation):
		num=random.randint(1,100)
		if num<simulation.probability_of_infection:
			self.is_infected=True

	def heal(self):
		self.is_infected=False
		self.days_infected=0

	def die(self):
		self.is_alive=False

	def update(self,simulation):
		if self.is_alive:
			if self.is_infected:
				self.days_infected+=1
				num=random.randint(1,100)
				if num<simulation.mortality_rate:
					self.die()
				elif self.is_alive:
					if self.days_infected==simulation.infection_durarion:
						self.heal()


class Population():
	def __init__(self,simulation):
		self.population=[]
		for i in range(0,simulation.population_size):
			person=Person()
			self.population.append(person)

	def initial_infection(self,simulation):
		infection_count=simulation.infected_percent*simulation.population_size
		infection_count=round(infection_count,0)
		infection_count=int(infection_count)
		for i in range(0,infection_count):
			self.population[i].is_infected=True
			self.population[i].days_infected=1
		random.shuffle(self.population)


	def spread_infection(self,simulation):
		for i in range(len(self.population)):
			if self.population[i].is_alive:
				if i==0:
					if self.population[i+1].is_infected:
						self.population[i].infect(simulation)
				elif i<len(self.population)-1:
					if self.population[i-1].is_infected or self.population[i+1].is_infected:
						self.population[i].infect(simulation)
				elif i==len(self.population)-1:
					if self.population[i-1].is_infected:
						self.population[i].infect(simulation)


	def update(self,simulation):
		simulation.day_number+=1
		for person in self.population:
			person.update(simulation)

	def display_stats(self,simulation):
		total_infected_count=0
		total_death_count=0
		for person in self.population:
			if person.is_infected:
				total_infected_count+=1
				if not person.is_alive:
					total_death_count+=1
		infected_percent=total_infected_count*100/simulation.population_size
		infected_percent=round(infected_percent,4)
		death_percent=total_death_count*100/simulation.population_size
		death_percent=round(death_percent,4)
		print(f'\nsummary of Day {simulation.day_number} : ')
		print(f'percentage of the population infected : {infected_percent}')
		print(f'percentage of the population that is dead : {death_percent}')
		print(f'total number of people infected : {total_infected_count}')
		print(f'total number of people dead : {total_death_count}')


	def graphics(self):
		status=[]
		print('\n')
		for person in self.population:
			if not person.is_alive:
				char='X'
			elif person.is_alive:
				if person.is_infected:
					char='I'
				else:
					char='O'
			status.append(char)
		for letter in status:
			print(letter,end='--')
		print('\n')
		print('O : heathy')
		print('I : infected')
		print('X : dead')





simulation=Simulation()
population=Population(simulation)
population.initial_infection(simulation)
population.display_stats(simulation)
population.graphics()
input('Press enter to start simulation!\n')
print('-------------------------------------------------')
for i in range(simulation.sim_days):
	population.spread_infection(simulation)
	population.update(simulation)
	population.display_stats(simulation)
	population.graphics()
	if i!=simulation.sim_days-1:
		input('Press enter to see next day simulation!!')
		print('-----------------------------------------------')
