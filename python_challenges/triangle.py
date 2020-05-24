print("Welcome to hypothenus finder App")
base=float(input("Enter the first leg:"))
height=float(input("Enter the second leg:"))
hypothenus=pow(((base*base)+(height*height)),0.5)
hypothenus=round(hypothenus,3)
area=0.5*base*height

print(f"The hypothenus of the triangle having {base} and {height} is {hypothenus}.")
print(f"The area is {area}.")