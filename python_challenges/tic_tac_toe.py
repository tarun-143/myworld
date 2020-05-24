def draw_board(char_list):
	print('\t   Tic-Tac-Toe')
	print('\t-----------------')
	print('\t|| '+str(char_list[0])+' || '+str(char_list[1])+' || '+str(char_list[2])+' ||')
	print('\t-----------------')
	print('\t|| '+str(char_list[3])+' || '+str(char_list[4])+' || '+str(char_list[5])+' ||')
	print('\t-----------------')
	print('\t|| '+str(char_list[6])+' || '+str(char_list[7])+' || '+str(char_list[8])+' ||')
	print('\t-----------------')
def player_input(n_list,char_list,player_char):
	while True:
		index=(input(f'\nEnter the place where you wnat to have {player_char} : '))
		if index in n_list:
			if int(index)>0 and int(index)<10:
				if char_list[int(index)-1]=='_':
					return int(index)
				else:
					print('That place has been already taken.')
			else:
				print('There is no such place on the board')
		else:
			print('Please enter a valid number from blank sots')
def replace(char_list,move,player):
	char_list[move-1]=player
def is_winner(player,blank_list):
	if ((blank_list[0]==player and blank_list[1]==player and blank_list[2]==player)
		 or 
		(blank_list[3]==player and blank_list[4]==player and blank_list[5]==player)
		 or 
		(blank_list[6]==player and blank_list[7]==player and blank_list[8]==player)
		 or 
		(blank_list[0]==player and blank_list[3]==player and blank_list[6]==player)
		 or 
		(blank_list[1]==player and blank_list[4]==player and blank_list[7]==player)
		 or 
		(blank_list[2]==player and blank_list[5]==player and blank_list[8]==player)
		 or 
		(blank_list[0]==player and blank_list[4]==player and blank_list[8]==player)
		 or 
		(blank_list[6]==player and blank_list[4]==player and blank_list[2]==player)):
	    return True
	else:
		return False



n_list=['1','2','3','4','5','6','7','8','9']
blank_list=['_']*9
draw_board(n_list)
print('\n')
draw_board(blank_list)
player_1='X'
player_2='O'
while True:
	move=int(player_input(n_list,blank_list,player_1))
	try:
		replace(blank_list,move,player_1)
		draw_board(n_list)
		draw_board(blank_list)
		result=is_winner(player_1,blank_list)
		if result:
			print('player_1 wins!')
			break
		if '_' not in blank_list:
			print('It is a tie!')
			break



		move=int(player_input(n_list,blank_list,player_2))
		try:
			replace(blank_list,move,player_2)
			draw_board(n_list)
			draw_board(blank_list)
			result=is_winner(player_2,blank_list)
			if result:
				print('player_2 wins!')
				break
		except ValueError:
			print('Please enter a valid number from blank slots')
	except ValueError:
		print('Please enter a valid number from blank slots')
print('Thanks for playing the game!')



