print("Welcome to the Calculator!")

# Prompt the user to input two numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (×)")
print("4. Division (÷)")

choice = input("Enter your choice (1/2/3/4): ")

# Perform the calculation based on the user's choice
if choice == '1':
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
elif choice == '2':
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
elif choice == '3':
    result = n1 * n2
    print(f"{n1} × {n2} = {result}")
elif choice == '4':
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = n1 / n2
        print(f"{n1} ÷ {n2} = {result}")
else:
    print("Invalid choice. Please try again.")
