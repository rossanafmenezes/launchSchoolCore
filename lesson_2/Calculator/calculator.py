# Step1 - Ask the user for the first number
# Step2 - Ask the user for the second number
# Step3 - Ask the user for the operation
# Step4 - Perform the operation
# Step5 - Display the result

# input validation check
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

# promp function
def prompt(message):
    print(f"==> {message}")
# Welcome the user to the calculator
print("Welcome to the calculator")

while True:
    # Step1 - Ask the user for the first number
    prompt('What\'s the first number?')
    number1 = input()

    while invalid_number(number1):
        prompt('Hummmmm... this does not look right. Please enter a valid number')
        number1 = input()

    # Step2 - Ask the user for the second number
    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt('Hummmmm... this does not look right. Please enter a valid number')
        number2 = input()

    print(f'You entered {number1} and {number2}')

    print("""
      What operation would you 
      like to perform? \n1) Add 2) Subtract 3) Multiply 4) Divide
      """
      )
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        print('Please select a valid option')
        operation = input()

    match operation:
        case '1':
            result = int(number1) + int(number2)
            print(f"The result is {result}")
        case '2':
            result = int(number1) - int(number2)
            print(f"The result is {result}")
        case '3':
            result = int(number1) * int(number2)
            print(f"The result is {result}")
        case '4':
            result = int(number1) / int(number2)
            print(f"The result is {result}")
        case _:
            print("Invalid operation")

    prompt('Would you like to performe another operation? (y/n)')
    answer = input()

    if answer and answer[0].lower != 'y':
        break
