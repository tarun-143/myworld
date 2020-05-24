name="       Tarun sayyapureddi"
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())

name=name.title().strip()
print(name)


firstname='meghana'
lastname='sayyapureddi'
fullname=firstname.upper()+ " " +lastname.upper()
print(fullname)

message="Hello,what are yoatu doing?"
count=message.lower().count("at")
print(count)

print("our message has",count,"s' in it",sep="{}")