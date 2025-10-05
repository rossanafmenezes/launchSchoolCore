def blah():
    pass

"""
1 - Countdown
Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down 
from 10 to 1 before launching.

Copy Code
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')
"""

# def decrease(counter):
#     return counter -1
#
# number = 10
# for _ in range(10):
#     print(number)
#     number = decrease(number)
#
# print('LAUNCH!')

"""
2 - Reverse a String
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected 
output. Explain the bug, and provide a solution.

def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")

"""
# Strings are immutable, so that line creates a new string each time by putting the current character in front of the
# current value of string. Because the loop’s iterator was built from the original value, the original characters still
# get iterated over, and you keep prepending to a growing copy that still contains the original text

# def reverse_string(string):
#     return string[::-1]
#
# print(reverse_string("hello") == "olleh")

"""
3 - Multiply List
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain 
the bug, and provide a solution.

Copy Code
def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

"""
# The reason why this is not working is because while you are multiplying each item in the list by 2, you are not actually
# reassigning the list items to the new value. Here is the solution:
#
# def multiply_list(lst):
#
#     for idx in range(len(lst)):
#         lst[idx] *= 2
#
#     return lst
#
# print(multiply_list([1, 2, 3]))
# print(multiply_list([1, 2, 3]) == [2, 4, 6])

"""
4 - Key Check
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising 
an error. Why is that? How would you fix this code?

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
"""
#The error is a keyerror because the key used is not present in the dictionary provided. We can fix it by either using
#dict.get(key) or by using a try-catch mechanism

# def get_key_value(my_dict, key):
#     return my_dict.get(key, None)
#
# print(get_key_value({"a": 1}, "b"))

"""
5 - Calendar Event Checker
We have a list of events and want to check whether a specific date is available (i.e., no events planned for that date).
However, the function always returns the wrong value.

Copy Code
events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True
"""

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

# def is_date_available(date):
#     if date not in events:
#         return True
#
#     return False
#
# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

"""
6 - Mutable Default Arguments
We want to create a function that appends a given value to a list. However, the function seems to be behaving 
unexpectedly:

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
How would you fix this code?

"""

# def append_to_list(value, lst=None):
#     if lst is None:
#         lst = []
#
#     lst.append(value)
#     return lst
#
# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])

"""
7 - Shadow
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. 
Why? How would you fix this code?


def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

"""
# def sum_and_multiply(numbers, factor):
#     return factor * sum(numbers)
#
# numbers = [1, 2, 3, 4]
# print(sum_and_multiply(numbers, 2))
# print(sum_and_multiply(numbers, 2) == 20)

"""
8 - Copy Issues
We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied 
list also seems to be affected:

import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])
What's wrong here? How can you fix it?

"""
#
# import copy
#
# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)
#
# original[0][0] = 99
#
# print(copied[0] == [1])

"""
9 - Set Modifications
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and 
how can we fix it?

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
"""
# Python does not allow you to change a set (or any mutable collection) while you iterate over it because it can make the loop unsatble. So we can
# iterate over a copy of the set. Here is how to fix it:

# data_set = {1, 2, 3, 4, 5}
#
# for item in data_set.copy():
#     if item % 2 == 0:
#         data_set.remove(item)
# print(data_set)

"""
10 - List Deduplication
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements 
is lost. How can we preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
"""

# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# # unique_data = list(set(data))
#
# def unique_data(data_lst):
#     unique_data_lst = []
#     for item in data_lst:
#         if item not in unique_data_lst:
#             unique_data_lst.append(item)
#     return unique_data_lst
#
# print(unique_data(data) == [4, 2, 1, 3]) # order not guaranteed
