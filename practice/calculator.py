num1 = int(input("enter a number1:"))
num2 = int(input("enter a number2:"))
operation = input("enter the operation:")

if operation == "+":
    print("sum :",num1 + num2)
elif operation == "-":
    print("diff:",num1 - num2)
elif operation == "*":
    print("product :",num1 * num2)
elif operation == "/":
    print("div:",num1 / num2)
else:
    print("invalid operation")