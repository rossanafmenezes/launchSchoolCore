# Question 1

numbers = [1, 2, 3, 4, 5]

reversed_list1 = numbers[::-1]
reversed_list2 = reversed(numbers)

print(numbers)
print(reversed_list1)
print(list(reversed_list2))

# Question 2

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False
number2 = 95 # True

print(number1 in numbers)
print(number2 in numbers)

# Question 3 

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

# Question 4
numbers = [1,2,3,4,5]
numbers.remove(numbers[2])
print(numbers)

# Question 5

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print( isinstance(numbers, list))
print( isinstance(table, list))

# Question 6

title = "Flintstone Family Members"
print(title.center(40))

# Question 7 

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count('t'))
print(statement2.count('t'))


# Question 8

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)

# Question 9 
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)

