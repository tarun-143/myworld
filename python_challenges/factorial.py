print('Welcome to factorial calculator')
num=int(input('the num u want to calculate the factorial:'))
print(str(num)+'! = ',end='')
de=''
for i in range(1,num):
	de=de+str(i)+'*'
print(de+str(num))
new=1
for i in range(1,num+1):
	new=new*i
print(f'the factorial of {num} is {new} !')