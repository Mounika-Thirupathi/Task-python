def calculator(a, b, choice):
    if choice == 1:
        print("Addition:", a + b)
    elif choice == 2:
        print("Subtraction:", a - b)
    elif choice == 3:
        print("Multiplication:", a * b)
    elif choice == 4:
        print("Integer Division:", a // b)
    elif choice == 5:
        print("Modulus:", a % b)
    else:
        print("Invalid choice!")

# Input values
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

# Display menu
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Integer Division")
print("5. Modulus")

# User choice
choice = int(input("Enter your choice (1-5): "))

# Call the calculator function
calculator(a, b, choice)
