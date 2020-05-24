import random
def printboard(char_list):
	print('\n\t-----------------')
	print(f'\t|| {char_list[0]} || {char_list[1]} || {char_list[2]} ||')
	print('\t-----------------')
	print(f'\t|| {char_list[3]} || {char_list[4]} || {char_list[5]} ||')
	print('\t-----------------')
	print(f'\t|| {char_list[6]} || {char_list[7]} || {char_list[8]} ||')
	print('\t-----------------')


def get_input(num_list,char_list,char):
	while True:
		move=input(f"where would you like to place {char} : ")
		if move in num_list:
			move = int(move)
			if char_list[move-1]=='_':
				return move
				break
			else:
				print('it has been already occupied!')
		else:
			print('There is no such index in the board!')



def replace_char(char_list,char,move):
	char_list[move-1]=char

def is_winner(player_char,char_list):
	if ((char_list[0]==player_char and char_list[1]==player_char and char_list[2]==player_char)
		 or 
		(char_list[3]==player_char and char_list[4]==player_char and char_list[5]==player_char)
		 or 
		(char_list[6]==player_char and char_list[7]==player_char and char_list[8]==player_char)
		 or 
		(char_list[0]==player_char and char_list[3]==player_char and char_list[6]==player_char)
		 or 
		(char_list[1]==player_char and char_list[4]==player_char and char_list[7]==player_char)
		 or 
		(char_list[2]==player_char and char_list[5]==player_char and char_list[8]==player_char)
		 or 
		(char_list[0]==player_char and char_list[4]==player_char and char_list[8]==player_char)
		 or 
		(char_list[6]==player_char and char_list[4]==player_char and char_list[2]==player_char)):
	    return True
	else:
		return False

def ai_move(num_list,char_list,player_char,computer_char):
	possible_moves=[]
	for i in num_list:
		i=int(i)
		if char_list[i-1]=='_':
			possible_moves.append(i)
	for move in possible_moves:
		replace_char(char_list,computer_char,move)
		if is_winner(computer_char,char_list):
			char_list[move-1]='_'
			return move
		else:
			char_list[move-1]='_'
	for move in possible_moves:
		replace_char(char_list,player_char,move)
		if is_winner(player_char,char_list):
			char_list[move-1]='_'
			return move
		else:
			char_list[move-1]='_'
	for move in possible_moves:
		if move==5:
			print(move)
			return move
	corners=[]
	for move in possible_moves:
		if move in [1,3,7,9]:
			corners.append(move)
	if len(corners)>0:
		move=random.choice(corners)
		print(move)
		return move
	edges=[]
	for move in possible_moves:
		if move in [2,4,6,8]:
			edges.append(move)
	if len(edges)>0:
		move=random.choice(edges)
		print(move)
		return move


char_list=['_']*9
num_list=['1','2','3','4','5','6','7','8','9']

while True:
	player_char=input('\nWould you like to choose "X" or "O" : ').lower()
	if player_char=='x':
		computer_char='O'
		break
	elif player_char=='o':
		computer_char='x'
		break
	else:
		print('You can only choose between X and O !')
if player_char=='x':
	printboard(num_list)
	printboard(char_list)
while True:
	if player_char=='x':
		move=get_input(num_list,char_list,player_char)
		print('Your move : ')
		replace_char(char_list,player_char,move)
		printboard(num_list)
		printboard(char_list)
		if is_winner(player_char,char_list):
			print('You won the game! you beat Mr.Computer! Congragulations!')
			break
		if '_' not in char_list:
			print('The game was a tie!')
			break
		print('Mr.Computer Move : ',end='')
		move=ai_move(num_list,char_list,player_char,computer_char)
		replace_char(char_list,computer_char,move)
		printboard(num_list)
		printboard(char_list)
		if is_winner(computer_char,char_list):
			print('You lost the game! Mr.Computer won agaist you! Better luck next time!')
			break
	else:
		print('Mr.Computer Move : ',end='')
		move=ai_move(num_list,char_list,player_char,computer_char)
		replace_char(char_list,computer_char,move)
		printboard(num_list)
		printboard(char_list)
		if is_winner(computer_char,char_list):
			print('You lost the game! Mr.Computer won agaist you! Better luck next time!')
			break
		if '_' not in char_list:
			print('The game was a tie!')
			break
		print('Your move : ')
		move=get_input(num_list,char_list,player_char)
		replace_char(char_list,player_char,move)
		printboard(num_list)
		printboard(char_list)
		if is_winner(player_char,char_list):
			print('You won the game! you beat Mr.Computer! Congragulations!')
			break