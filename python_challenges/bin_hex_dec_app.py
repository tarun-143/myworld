print('Welcome to the App')

max_value=int(input("what is the max value u want to print numbers:"))

binary=[]
hexa=[]

for num in range(1,max_value+1):
	binary.append(bin(num))
	hexa.append(hex(num))

print("we want to show a portion of list")
print('\n')
start=int(input("enter the num where you want to start slicing:"))
stop=int(input("enter the num where you want to stop slicing:"))


print('the format is: number........binary.......hexadecimal.')
for num in range(start,stop+1):
	print(f'{num}.........{bin(num)}..........{hex(num)}')
input('press entr to see the full list from 1 to '+str(max_value))

for nu,num,numb in zip(range(1,max_value+1),binary,hexa):
	print(str(nu)+'----------------'+str(num)+'------------------'+str(numb))



