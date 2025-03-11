num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
operand = input("What operation do you want to perform?")

result = 0
if operand == "+":
    result = num1 + num2
    print(num1, operand, num2, "=", result)
elif operand == "-":
    result = num1 - num2
    print(num1, operand, num2, "=", result)
elif operand == "*":
    result = num1 * num2
    print(num1, operand, num2, "=", result)
elif operand == "/":
    result = num1 / num2
    print(num1, operand, num2, "=", result)
else:
    print("You entered an incorrect operand!")