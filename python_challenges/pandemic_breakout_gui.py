import tkinter
import random
import math
class Simulation():
	def __init__(self):
		self.day_number=1
		self.population_size=int(input('\nEnter the population_size of the city : '))
		root=math.sqrt(self.population_size)
		if int(root+0.5)**2!=self.population_size:
			root=int(round(root,0))
			self.grid_size=root
			self.population_size=(self.grid_size)**2
			print('The nearest perfect square is taken for visual purposes!')
		else:
			self.grid_size=int(math.sqrt(self.population_size))


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



class Population:
	def __init__(self,simulation):
		self.population=[]
		for i in range(0,simulation.grid_size):
			row=[]
			for i in range(0,simulation.grid_size):
				person=Person()
				row.append(person)
			self.population.append(row)

	def initial_infection(self,simulation):
		infected_count=simulation.infected_percent*simulation.population_size
		infected_count=int(round(infected_count,0))
		infections=0
		while infections<infected_count:
			x=random.randint(0, simulation.grid_size - 1)
			y=random.randint(0, simulation.grid_size - 1)
			person=self.population[x][y]
			if not person.is_infected:
				person.is_infected=True
				person.days_infected=1
				infections+=1


	def spread_infection(self,simulation):
		for i in range(0,simulation.grid_size):
			for j in range(0,simulation.grid_size):
				if self.population[i][j].is_alive:
					if i==0:
						if j==0:
							if self.population[i][j+1].is_infected or self.population[i+1][j]:
								self.population[i][j].infect(simulation)
						elif j==simulation.grid_size-1:
							if self.population[i+1][j].is_infected or self.population[i][j-1].is_infected:
								self.population[i][j].infect(simulation)
						else:
							if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i][j-1].is_infected:
								self.population[i][j].infect(simulation)
					elif i==simulation.grid_size-1:
						if j==0:
							if self.population[i][j+1].is_infected or self.population[i-1][j]:
								self.population[i][j].infect(simulation)
						elif j==simulation.grid_size-1:
							if self.population[i-1][j].is_infected or self.population[i][j-1].is_infected:
								self.population[i][j].infect(simulation)
						else:
							if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i][j-1].is_infected:
								self.population[i][j].infect(simulation)
					else:
						if j==0:
							if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
								self.population[i][j].infect(simulation)
						elif j==simulation.grid_size-1:
							if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
								self.population[i][j].infect(simulation)
						else:
							if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected or self.population[i][j+1].is_infected :
								self.population[i][j].infect(simulation)


	def update(self,simulation):
		simulation.day_number+=1
		for i in range(0,simulation.grid_size):
			for j in range(0,simulation.grid_size):
				self.population[i][j].update(simulation)

	def display_stats(self,simulation):
		total_infected_count=0
		total_death_count=0
		for i in range(0,simulation.grid_size):
			for person in self.population[i]:
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
		print('\n--------------------------------------------------------')

def graphics(simulation,popu,canvas):
	square_size=600//simulation.grid_size
	for i in range(0,simulation.grid_size):
		y=i*square_size
		for j in range(0,simulation.grid_size):
			x=j*square_size
			if not popu.population[i][j].is_alive:
				canvas.create_rectangle(x,y,x+square_size,y+square_size,fill='red')
			elif popu.population[i][j].is_infected:
				canvas.create_rectangle(x,y,x+square_size,y+square_size,fill='yellow')
			else:
				canvas.create_rectangle(x,y,x+square_size,y+square_size,fill='green')


simulation=Simulation()
WINDOW_HEIGHT=600
WINDOW_WIDTH=600
sim_win=tkinter.Tk()
sim_win.title('Pndemic OutBreak')
sim_canvas=tkinter.Canvas(sim_win,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)
population=Population(simulation)
population.initial_infection(simulation)
population.display_stats(simulation)
input('\npress enter to begin simulation!')
print('------------------------------------------------')
for i in range(simulation.sim_days):
	population.spread_infection(simulation)
	population.update(simulation)
	population.display_stats(simulation)
	graphics(simulation,population,sim_canvas)
	sim_win.update()
	if i != simulation.sim_days-1:
		sim_canvas.delete('all')

























