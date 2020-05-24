print("Welcome to Temperature conversion App")

temp_f=float(input("Enter the temperature in fareinheit:"))

temp_c=5/9*(temp_f-32)

temp_k=temp_c+273.15

print(f"Temperature in celcius:\t\t {temp_c}.")
print(f"Temperature in fareinheit:\t {temp_f}.")
print(f"Temperature in kelvin:\t\t {temp_k}.")