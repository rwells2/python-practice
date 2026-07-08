"""
Challenge 8: Calculator

Create functions

add()

subtract()

multiply()

divide()

Have the user choose an operation.

Example

Choose:

1 Add

2 Multiply

3 Divide
"""

def main():
    choice = input("Choose whether you would like to add, subtract, multiply, or divide: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if (choice.lower() == "add"):
        print(add(num1, num2))
    elif (choice.lower() == "subtract"):
        print(subtract(num1, num2))
    elif (choice.lower() == "multiply"):
        print(multiply(num1, num2))
    elif (choice.lower() == "divide"):
        print(divide(num1, num2))
    else:
        print("Option not available")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    main()
