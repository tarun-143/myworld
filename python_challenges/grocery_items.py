import datetime

time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)
print('welcome to our grcery')

print(f'current date and time: {month}/{day}   and    {hour}:{minute} ')
foods=['Meat','Cheese']

print("you currnetly hve"+ " " +foods[0]+" "+ foods[1])

food=input("\n item u want to add:")
foods.append(food.title())
food=input("\n item u want to add:")
foods.append(food.title())
food=input("\n item u want to add:")
foods.append(food.title())
print('here is ur sorted grocery list....')
foods.sort()
print(foods)


buy=input("\n item u want to buy:").title()
print(f'removing {buy} from grocery')
foods.remove(buy)
print(f'current grocery: {foods}')

buy=input("\n item u want to buy:").title()
print(f'removing {buy} from grocery')
foods.remove(buy)
print(f'current grocery: {foods}')

buy=input("\n item u want to buy:").title()
print(f'removing {buy} from grocery')
foods.remove(buy)
print(f'current grocery: {foods}')

no_item=foods.pop()

print(f'\nsorry.we are out of {no_item}')











