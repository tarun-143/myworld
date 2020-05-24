import random
print('-----------------------PowerBall---------------------')
w_b=int(input('How many white balls to draw for 5 winning numbers:(normally 69):'))
try:
	r_b=int(input('How many red balls to draw for 1 power ball(normally 26);'))
	try:
		while True:
			winning_white_tickets=[]
			while(len(winning_white_tickets)!=5):
				choice=random.randint(1,w_b)
				if choice not in winning_white_tickets:
					winning_white_tickets.append(choice)
			power_ball=random.randint(1,r_b)
			inter=int(input('IN what interval do u want to purchase tickets:'))
			print('---------------------welcome  to power_ball--------------------')
			print('tonights winning numbers are:')
			print('white_ball tickets:')
			for el in winning_white_tickets:
				print(el,end=' ')
			print(f'power ball:{power_ball} ')
			i=1
			tickets=[]
			while(i!=inter+1):
				ticket=[]
				while(len(ticket)!=5):
					num=random.randint(1,w_b)
					if num not in ticket:
						ticket.append(num)
				power_ball_ticket=random.randint(1,r_b)
				if ticket==winning_white_tickets and power_ball==power_ball_ticket:
					print(f'Congragulations!you won the ticket you bought {i} tickets! ')
				
			choice=input('DO u wnat to play agin!(y/n)').lower()
			if choice=='n':
				break
	except ValueError:
		print('please give valid input!')
except ValueError:
	print('please give valid input')



