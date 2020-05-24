print("Welcome to the Letter Counter App")
name=input("what is your name:")
print(f'Hello {name}')
print("\n")
print('I will count number of letters in your message')
print("\n")

message=input("Please enter the message:")
Letter=input("which Letter:")

count=message.count(Letter)

print(f'your message has {count} {Letter} in it.')
