import random
game_dict={
	"sports":['basketball', 'baseball', 'soccer', 'football', 'tennis'],
	"colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet'],
	"fruits":['apple', 'banana', 'watermelon', 'peach', 'mango'],
	"classes":['english', 'history', 'science', 'mathematics', 'art']
}
game_keys=[]
for key in game_dict:
	game_keys.append(key)
while True:
	category=game_keys[random.randint(0,len(game_keys)-1)]
	word=game_dict[category][random.randint(0,len(game_dict[category])-1)]
	blank_word=[]
	for letter in word:
		blank_word.append('_')
	print(f'Guess the {len(word)} letter word from category {category} ')
	guess_count=0
	while True:
		Guess=input('\nenter your guess:').lower()
		guess_count+=1
		if Guess==word:
			print(f'congragulation! you took {guess_count} guesses!')
			break
		else:
			print('\nyour guess is incorrect! Try to find with a clue')
			while True:
				if '_' not in blank_word:
					print(f'you falied to guess the word {word}!')
					break
				index=random.randint(0,len(word)-1)
				if blank_word[index]=='_':
					blank_word[index]=word[index]
					for wor in blank_word:
						print(wor,end=' ')
					break
		if '_' not in blank_word:
			print(f'\nyou falied to guess the word {word}!')
			break
	choice=input('\nDo u want to play again(y/n:)').lower()
	if choice=='y':
		continue
	else:
		break
print('Thank You playing the game!')

