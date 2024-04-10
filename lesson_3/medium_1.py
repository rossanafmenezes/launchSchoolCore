# Question 1

# def ascii_art(number):
#     for n in range(1, number):
#         print(' ' *n + 'The Flintstones Rock!')

# ascii_art(10)

# # Question 2

# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# print(factors(-20)) 

# The purpose it to determine if there's no remainder to the division. If there
# isn't, the number is a factor

#Question 3

# The first method mutates the original list the second creates a new list

# Question 4

# 0.8999999999999999
# False

# Question 5

# The result is false because NaN is equal to nothing
#This includes itself

# Question 6

# It returns 34 because even tho the fact that you pass answer as an argument 
# of the method it does not mutate the orginal variable. 

# Question 7

#Yes because dicts are mulatble

# Question 8

# Paper

# Question 9

# No

#Question 10
# True

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True


print(is_an_ip_number('12345'))