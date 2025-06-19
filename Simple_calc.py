#build a calculator in python
#it should ask the user for the first and second number
#then ask the user to input an operator
#calculation is then done based on the chosen operator
#DO NOT use TRY EXCEPT
#BONUS: avoid parsing an invalid number string
#BONUS: ensure that your program doesnt get a 0 division error




def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter the Operator: ")
    if operator == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif operator == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operator == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operator == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid operator")

except Exception as e:
    print(f"Exception occurred: {e}")
    print(f"An error occurred: {e}")




