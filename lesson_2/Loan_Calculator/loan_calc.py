import json

# Check for input validation
def invalid_number(number_str):
    try:
        if float(number_str) <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True
    return False

def message(message, lang='en'):
    return MESSAGES[lang][message]

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(message('welcome'))
print('<----------------->')

print(message('loan_amount'))
loan_amount = input()
while invalid_number(loan_amount):
    print('Please enter a valid number. Amount must be greater than 0')
    loan_amount = input()


print(message('interest_rate'))
interest_rate = input()
while invalid_number(interest_rate):
    print('Please enter a valid number. Rate must be greater than 0')
    interest_rate = input()


print(message('loan_duration'))
loan_duration = input()
while invalid_number(loan_duration):
    print('Please enter a valid number. Duration must be greater than 0')
    loan_duration = input()    

amount_float = float(loan_amount)
annual_rate = float(interest_rate) / 100
monthly_rate = annual_rate / 12
duration_months = float(loan_duration) * 12

monthly_payment = amount_float * (
        monthly_rate /
            (1 - (1 + monthly_rate) ** (-duration_months))
    )

print(message('result') + f'{monthly_payment:.2f}')
