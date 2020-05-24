import random
h=0
t=0

choices=['HEADS','TAILS']
trails=int(input('how many times u want to flip a coin:'))
for num in range(1,trails+1):
	choice=random.choice(choices)
	if choice=='HEADS':
		h+=1
	if choice=='TAILS':
		t+=1
	print(choice)
	if h==t:
		print(f'At trail {num} the number of heads are equal to number of tails {h} each.')
print('summary of the flips:')
print(f'No of heads = {h}')
print(f'No of tails = {t}')
Heads_percentage = (h/num)*100
Tails_percentage = (t/num)*100
print(f'Heads percentage = {round(Heads_percentage,2)}')
print(f'Tails percentage = {round(Tails_percentage,2)}')