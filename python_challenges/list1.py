names=['tarun','varun','arun','karun']
#temporary sorting to that paricular line
print(sorted(names))
#no change if:
sorted(names)
print(sorted(names,reverse=True))
#permanat sorting

names.sort()
print(names)

names.sort(reverse=True)
print(names)

#tuples are enclosed by () and they have no attributes such as append,reverse,sort.....

word="hello world"
list_word=list(word)
print(word)
print(list_word)
numbers=list(range(10,101,10))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))


#if we assingn one list to other the change in one list effects both the lists so use copy function
nums=numbers.copy()