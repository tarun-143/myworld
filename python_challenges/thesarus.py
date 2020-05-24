import random
print('Welcome to the Thesarus App')
print('select a word from below list of words:')
synonyms={
	'hot':['red','heated','torrid','humid'],
	'cold':['crisp','frigid','wintry','raw'],
	'happy':['cheerful','merry','pleasant','glad'],
	'sad':['bitter','dismal','mournful','somber']
}
for key in synonyms.keys():
	print(f'\t-{key}')
select=input('select a word:').lower().strip()
if select in synonyms.keys():
	index=random.randint(0,3)
	print(f'The synonym of {select.title()} is {synonyms[select][index].title()} ')
else:
	print(f'{select.title()} is not in the list')
con=input('Do You wnat to see the whole Thesarus(y/n):').lower()
if con=='y':
	print('here is the list')
	for keys,values in synonyms.items():
		print('synonym of'+keys+':')
		for value in values:
			print(f'\t-{value}')
else:
	print('Hope you learned a new synonym!')