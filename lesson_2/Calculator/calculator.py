# Step1 - Ask the user for the first number
# Step2 - Ask the user for the second number
# Step3 - Ask the user for the operation
# Step4 - Perform the operation
# Step5 - Display the result

# Welcome the user to the calculator
print("Welcome to the calculator")

# Step1 - Ask the user for the first number
print('What\'s the first number?')
number1 = input()

# Step2 - Ask the user for the second number
print("What's the second number?")
number2 = input()

print(f'You entered {number1} and {number2}')

print("What operation would you like to perform? \n1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

if operation == '1':
    result = int(number1) + int(number2)
    print(f"The result is {result}")
elif operation == '2':
    result = int(number1) - int(number2)
    print(f"The result is {result}")
elif operation == '3':
    result = int(number1) * int(number2)
    print(f"The result is {result}")
elif operation == '4':
    result = int(number1) / int(number2)
    print(f"The result is {result}")
else:
    print("Invalid operation")