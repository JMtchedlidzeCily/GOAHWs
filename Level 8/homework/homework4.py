# Get input from the user
num1 = int(input("Enter the value for num1: "))
num2 = int(input("Enter the value for num2: "))

# Compare
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
