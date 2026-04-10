#Simple Calculator

num1 = float(input("Enter the first number: "))
opr = input("select the operators ie. +, -,*,%")
num2 = float(input("Enter the second number: "))

if opr == '+':
    result = num1 + num2
elif opr == '-':
    result = num1 - num2
elif opr == '*':
    result = num1 * num2
elif opr == '%':
    result = num1 % num2

print("The result is: ",result)