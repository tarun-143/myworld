from matplotlib import pyplot
print('Welcome to the loan caculator')
def loan_info():
	loan_info={}
	loan_info['principle']=float(input('Enter the principle amount : '))
	loan_info['intrest']=float(input('Enter the percent of yearly intrest : '))
	loan_info['monthly_paid']=float(input('Enter the monthly-paid desiered amount : '))
	loan_info['money_paid']=0
	return(loan_info)
def calculator(diction):
	diction['principle']=((diction['principle']*diction['intrest']/100)/12)+diction['principle']-diction['monthly_paid']
	diction['money_paid']+=diction['monthly_paid']
def information(dictionary,month_counter,base):
	print(f'----------------loan details after {month_counter} months-------------------')
	for key,value in dictionary.items():
		print(f'\t{key} : {value}')
def ceate_graph(data_to_plot,start):
	x_values=[]
	y_values=[]
	for point in data_to_plot:
		x_values.append(point[0])
		y_values.append(point[1])
	pyplot.plot(x_values,y_values)
	pyplot.title(str(start['intrest'])+'%' +' intrest with '+str(start['monthly_paid']) +'payment' )
	pyplot.xlabel('Month number')
	pyplot.ylabel('principle amount')
	pyplot.show()
start=loan_info()
starting_principle=start['principle']
month_counter=0
data=[]
while True:
	information(start,month_counter,starting_principle)
	data.append((month_counter,start['principle']))
	if start['principle']>starting_principle:

		print('\nyou cannot get rid of the intrest')
		print('you can never clear yor debt')
		break
	calculator(start)
	month_counter+=1
	if start['principle']<=0:
		print(f'\nYou paid total amount in {month_counter} months')
		print('Total money_paid = '+ str(start['money_paid']))
		total_intrest=start['money_paid']-starting_principle
		print(f'money_paid on intrest = '+str(total_intrest))
		ceate_graph(data,start)
		break

