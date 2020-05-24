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
for key in sorted_dict_1:
	print(key[0],end=' ')

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
for key in sorted_dict_2:
	print(key[0],end=' ')
