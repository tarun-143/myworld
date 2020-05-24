import random
class Player():
	def __init__(self,total_bet,table_bet,cards):
		self.total_bet=total_bet
		self.table_bet=table_bet
		self.is_winner=False
		self.total_value=0
		self.cards=cards
		self.is_ace=True
		self.Player_cards=[]
		self.Player_card_values=[]
	def card_selection(self,cards):
		category=cards[random.randint(0,3)]
		card=str(category[random.randint(0,12)])
		if card=='J' or card=='K' or card=='Q':
			card='10'
		if card=='A' and self.is_ace:
			card='11'
		else:
			card='1'
		des=f'{card} of {category} '
		self.Player_cards.append(des)

	def total_card_value(self):
		for card in self.Player_card_values:
			self.total_value+=int(card)

	def is_winner(self):
		if self.total_value>21:
			is_winner=False
			self.total_bet-=self.table_bet


	def ace_value(self):
		if self.total_value>21:
			self.is_ace=False
		else:
			self.is_ace=True

	def show_values(self,cards):
		print(f'current Amount : {self.total_bet}')
		print(f'table_bet : {self.table_bet}')
		print('cards in Player hand:')
		for card in self.Player_cards:
			print(f'card')
		print(f'total value : {self.total_value} ')

class Dealer():
	def __init__(self,cards):
		self.is_winner=False
		self.total_value=0
		self.cards=cards
		self.is_ace=True
		self.dealer_cards=[]
		self.dealer_card_values=[]
	def card_selection(self,cards):
		category=cards[random.randint(0,3)]
		card=f'{str(category[random.randint(0,12)])} of {category} '
		if card=='J' or card=='K' or card=='Q':
			card='10'
		if card=='A' and self.is_ace:
			card='11'
		else:
			card='1'
		des=f'{card} of {category} '
		self.dealer_cards.append(des)

	def total_card_value(self):
		for card in self.dealer_card_values:
			self.total_value+=int(card)

	def is_winner(self):
		if self.total_value>21:
			is_winner=False
	def one_card(self):
		dealer_card=self.dealer_cards[random.randint(0,1)]
		print(f'dealer is showing {dealer_card}')
	def reveal_cards(self):
		for card in self.dealer_cards:
			print(card)


spades=['A','2','3','4','5','6','7','8','9','10','K','J','Q']
clubs=['A','2','3','4','5','6','7','8','9','10','K','J','Q']
diamonds=['A','2','3','4','5','6','7','8','9','10','K','J','Q']
hearts=['A','2','3','4','5','6','7','8','9','10','K','J','Q']
cards=[spades,hearts,clubs,diamonds]
print('Welcome to blackJack app')
total_bet=int(input('What is the total bet today:'))
table_bet=int(input('what is the bet for this table:'))
player=Player(total_bet,table_bet,cards)
dealer=Dealer(cards)
print(type(dealer.dealer_cards))  
for i in range(0,2):
	player.card_selection(cards)
	dealer.card_selection(cards)
while True:
	dealer.one_card()
	print(type(dealer.total_card_value()))
	player.total_card_value()
	player.show_values(cards)
	break
