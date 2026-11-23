print("Cli Calculator")

# Enter first number
num1 = float(input("Enter first number: "))
# Enter second number
num2 = float(input("Enter second number: "))

# Enter operation
operation = input("Enter operation Add (a), Subtract (s), Multiply (m), Divide (d): ")

# Add, subtract, multiply, or divide based on the operation

if operation == "a":
    result = num1 + num2
elif operation == "s":
    result = num1 - num2
elif operation == "m":
    result = num1 * num2
elif operation == "d":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(f"Result: {result}")
