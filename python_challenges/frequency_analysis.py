import operator
print('Welcome to the Frequency Analysis App')
phrase=input('Enter the phrase which is to be analysed:')
results={}
for letter in phrase:
	if letter==' ':
		continue
	if letter in results.keys():
		results[letter]['occur']+=1
	else:
		results[letter]={
		'occur':1
		}
total_letters=0
for letter in phrase:
	if letter==' ':
		continue
	else:
		total_letters+=1
for key in results:
	results[key]['percent']=(results[key]['occur']/total_letters)*100
	results[key]['percent']=round(results[key]['percent'],2)
print('\tletter'+'\t   occurance'+'\t   frequency')
for key,value in results.items():
	print('\n')
	print(f'\t   {key}',end=' ')
	for item in value:
		print('\t'+'      '+str(value[item]),end=' ')
sorted_list={}
for key in results:
	sorted_list[key]=results[key]['occur']
sorted_dict = sorted(sorted_list.items(), key=operator.itemgetter(1),reverse=True)
print('\n')
print('From highest to lowest the occurance of the letters:')
for key in sorted_dict:
	print(key[0],end='')

