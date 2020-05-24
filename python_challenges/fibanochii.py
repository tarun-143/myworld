a=1
b=1
c=0
series=[1,1]
num=int(input('no:'))
print(a)
print(b)
for i in range(1,num-1):
	c=a+b
	a=b
	b=c
	series.append(c)
	print(c)
print('\n')
for i in range(num-1):
	value=series[i]/series[i+1]
	print(value)
value=round(value,4)
print('the value of phi is'+' '+ str(value))
