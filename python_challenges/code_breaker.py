import operator
from collections import Counter
print('\nWelcome to the Frequency Analysis App')
phrase_1='qwertyuiopasdfghkkljmnbvcxzuhsfusnnsngfirsyrruwf'
non_letters=[" ",'!',"@","#","$","%","^",'&','&','*','(',')','-','_','=',"+",',','.','<','>',"'",';',':','[',']','{','}','|','?','/']
for letter in phrase_1:
	if letter in non_letters:
		phrase_1=phrase_1.replace(letter,'')
total_letters_1=len(phrase_1)
dicti_1=Counter(phrase_1)
print('\n')
print('\tletter'+'\t\toccurance'+'\tfrequency')
for key in Counter(phrase_1):
	print(f'\t  {key}\t\t  {dicti_1[key]}\t\t  {round((dicti_1[key]*100/total_letters_1),2)} ')
sorted_dict_1 = Counter(phrase_1).most_common(total_letters_1)
print('\n')
print('From highest to lowest the occurance of the letters:')
list_1=[]
for key in sorted_dict_1:
	print(key[0],end=' ')
	list_1.append(key[0])

phrase_2='mnbvcxzasdfghjklpoiuytrewqxhjgdbrufbgusfdhfbsjrb'
non_letters=[" ",'!',"@","#","$","%","^",'&','&','*','(',')','-','_','=',"+",',','.','<','>',"'",';',':','[',']','{','}','|','?','/']
for letter in phrase_2:
	if letter in non_letters:
		phrase_2=phrase_2.replace(letter,'')
total_letters_2=len(phrase_2)
dicti_2=Counter(phrase_2)
print('\n')
print('\tletter'+'\t\toccurance'+'\tfrequency')
for key in Counter(phrase_2):
	print(f'\t  {key}\t\t  {dicti_2[key]}\t\t  {round((dicti_2[key]*100/total_letters_2),2)} ')
sorted_dict_2 = Counter(phrase_2).most_common(total_letters_2)
print('\n')
print('From highest to lowest the occurance of the letters:')
list_2=[]
for key in sorted_dict_2:
	print(key[0],end=' ')
	list_2.append(key[0])
print('\n')
list_1.append(' ')
list_2.insert(5,' ')
non_letters=['!',"@","#","$","%","^",'&','&','*','(',')','-','_','=',"+",',','.','<','>',"'",';',':','[',']','{','}','|','?','/']
option=input('\ndo you wnat to  encode or decode a message:').lower()
if option=='encode':
	encode=input('Enter the message which is to be encoded:')
	for letter in encode:
		if letter in non_letters:
			encode=encode.replace(letter,'')
	encoded_phrase=[]
	for letter in encode:
		index=list_1.index(letter)
		letter=list_2[index]
		encoded_phrase.append(letter)
	print('The encoded message is:',end='')
	for letter in encoded_phrase:
		print(letter,end='')
elif option=='decode':
	decode=input('Enter the message which is to be decoded:')
	for letter in decode:
		if letter in non_letters:
			decode=decode.replace(letter,'')
	decoded_phrase=[]
	for letter in decode:
		index=list_2.index(letter)
		letter=list_1[index]
		decoded_phrase.append(letter)
	print('The decoded message is:',end='')
	for letter in decoded_phrase:
		print(letter,end='')
else:
	print('Please give encode or decode.Try Again!')
