import random
import time
class Card():
	def __init__(self,rank,value,suit):
		self.rank=rank
		self.value=value
		self.suit=suit


	def display_card(self):
		print(f'{self.rank} of {self.suit}')



class Deck():
	def __init__(self):
		self.cards=[]

	def build_deck(self):
		suits=['Spades','Hearts','Diamonds','Clubs']
		ranks={
		'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10,'A':11
		}
		for suit in suits:
			for rank,value in ranks.items():
				card=Card(rank,value,suit)
				self.cards.append(card)


	def shuffle_cards(self):
		random.shuffle(self.cards)


	def deal_card(self):
		card=self.cards.pop()
		return card

class Player():
	def __init__(self):
		self.hand_value=0
		self.hand=[]
		self.playing_hand=True


	def draw_hand(self,deck):
		for i in range(0,2):
			card=deck.deal_card()
			self.hand.append(card)


	def display_hand(self):
		print('\ncards in players hands : ')
		for card in self.hand:
			card.display_card()


	def hit(self,deck):
		card=deck.deal_card()
		self.hand.append(card)


	def get_hand_value(self):
		self.hand_value=0
		is_ace_in_hand=False
		for card in self.hand:
			self.hand_value+=card.value
			if card.rank=='A':
				is_ace_in_hand=True
		if self.hand_value>21 and is_ace_in_hand:
			self.hand_value-=10
		print(f'Total_value : {self.hand_value}')


	def update_hand(self,deck):
		if self.hand_value<21:
			choice=input('\nWould you like to hit (y/n) : ').lower()
			if choice=='y':
				self.hit(deck)
			else:
				self.playing_hand=False
		else:
			self.playing_hand=False


class Dealer():
	def __init__(self):
		self.hand_value=0
		self.hand=[]
		self.playing_hand=True

	def draw_hand(self,deck):
		for i in range(0,2):
			card=deck.deal_card()
			self.hand.append(card)


	def display_hand(self):
		input("Press enter to reveal delear's hand")
		print('\n')
		for card in self.hand:
			card.display_card()
			time.sleep(1)


	def hit(self,deck):
		self.get_hand_value()
		while self.hand_value<17:
			card=deck.deal_card()
			self.hand.append(card)
			self.get_hand_value()
		print('\nThe Dealer has a set of '+str(len(self.hand)))


	def get_hand_value(self):
		self.hand_value=0
		is_ace_in_hand=False
		for card in self.hand:
			self.hand_value+=card.value
			if card.rank=='A':
				is_ace_in_hand=True
		if self.hand_value>21:
			self.hand_value-=10

class Game():
	def __init__(self,amount_of_money):
		self.amount_of_money=amount_of_money
		self.bet=20
		self.winner=''

	def set_bet(self):
		betting=True
		while betting:
			bet=int(input('\nWhat is the bet of this table : '))
			if bet<10:
				bet=20
			if bet>self.amount_of_money:
				print('You cannot afford '+str(bet))
			else:
				self.bet=bet
				betting=False
	def scoring(self,player_hand_value,dealer_hand_value):
		if player_hand_value==21:
			print('player got black jack.......you won')
			self.winner='p'
		elif dealer_hand_value==21:
			print('dealer got black jack......dealer won')
			self.winner='d'
		elif player_hand_value>21:
			print('player got over 21......dealer won')
			self.winner='d'0
		elif dealer_hand_value>21:
			print('dealer got over 21.........player won')
			self.winner='p'
		else:
			if player_hand_value>dealer_hand_value:
				print('dealer gets '+str(dealer_hand_value)+'points.......you won!')
				self.winner='p'
			elif player_hand_value<dealer_hand_value:
				print('dealer gets '+str(dealer_hand_value)+'points.......dealer won!')
				self.winner='d'
			else:
				print('it is a tie both got '+str(dealer_hand_value)+ 'points')


	def payout(self):
		if self.winner=='p':
			self.amount_of_money+=self.bet
		elif self.winner=='d':
			self.amount_of_money-=self.bet


	def display_money(self):
		print(f'current money : {self.amount_of_money}')

	def display_money_and_bet(self):
		print(f'\ncurrent money : {self.amount_of_money}                 current bet : {self.bet}')


print('\nWelcome to the black jack Game!')
amount_of_money=int(input('What is today bet : '))
game=Game(amount_of_money)
while True:
	game.display_money()
	game.set_bet()
	game.display_money_and_bet()
	deck=Deck()
	deck.build_deck()
	deck.shuffle_cards()
	dealer=Dealer()
	dealer.draw_hand(deck)
	player=Player()
	player.draw_hand(deck)
	print(f'delear is showing  {dealer.hand[0].rank} of {dealer.hand[0].suit}')
	while player.playing_hand:
		player.display_hand()
		player.get_hand_value()
		player.update_hand(deck)

	dealer.hit(deck)
	dealer.display_hand()
	game.scoring(player.hand_value,dealer.hand_value)
	game.payout()
	if game.amount_of_money<20:
		print('sorry you ran out of money')
		break