print("Welcome to the grade-sorter app")

grades=[]

grades.append(input("enter your first grade:"))
grades.append(input("enter your second grade:"))
grades.append(input("enter your third grade:"))
grades.append(input("enter your fourth grade:"))

print(f"your grades are {grades}")

print(f"your grades from highest to lowest are {grades.sort(reverse=True)}")

print('your lowest two grades are dropped')
print('\n')
print(f"removed grade:{grades.pop()}.")
print('\n')
print(f'removed grade:{grades.pop()}')
print('\n')
print(f'your remaining grades are:{grades}')
print(f'your highest grade is {grades[0]}.')