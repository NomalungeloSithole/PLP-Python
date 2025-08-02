#A simple calculator program that performs arithmetic operations

firstNumber = float(input("Please enter the first number:"))
secondNumber = float(input("Please enter the second number:"))
operation = input("Select which operation you would like to perform: (+,-,*,/,**)")

if operation == "+":
    solution = firstNumber + secondNumber
    print(f"\nThe result is: {solution}")
elif operation == "-":
    solution = firstNumber - secondNumber
    print(f"\nThe result is: {solution}")
elif operation == "*":
    solution = firstNumber * secondNumber
    print(f"\nThe result is: {solution}")
elif operation == "/":
    if secondNumber != 0:
        solution = firstNumber / secondNumber
    else:
        print("The denominator cannot be zero!")
    print(f"\nThe result is: {solution}")
elif operation == "**":
    solution = firstNumber ** secondNumber
    print(f"\nThe result is: {solution}")

