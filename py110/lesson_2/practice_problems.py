# # Given the list numbers = [10, 3, 7, 1, 9], use sorted to return a new list sorted in descending order.
#
# numbers = [10, 3, 7, 1, 9]
# print(numbers)
# new_numbers = sorted(numbers, reverse = True)
# print(numbers)
# print(new_numbers)
#
# # Sort the list of strings words = ['Banana', 'apple', 'Cherry', 'date'] in a case-insensitive way.
#
# words = ['Banana', 'apple', 'Cherry', 'date']
#
# print(sorted(words, key=str.lower))
#
# # You have a list of tuples representing people and their ages: people = [('Alice', 30), ('Bob', 25), ('Charlie', 25)].
# Sort this list first by age, then by name.
#
# people = [('Alice', 30), ('Bob', 25), ('Charlie', 25)]
#
# def sort_age(person):
#     name, age = person
#     return age, name
#
# print(sorted(people, key=sort_age))
#
# # Given the string s = "banana", create a new string with its characters sorted alphabetically.
# s = "banana"
# b = "oranges"
# print(sorted(list(s)))
#
# # Write a function that takes a list of words and returns a new list sorted by the length of each word, shortest to
# longest.
# def sort_len(word):
#     return len(word)
#
# print(sorted(words, key=sort_len))
#
# #Given the list , use sorted to sort it. What order do you expect and why?
# """
# A, C, b, d because uppercase letters come before lowercase letters in the ASCII table
# """
# mixed = ['b', 'A', 'd', 'C']
#
# #Given a list of dictionary keys keys = ['D', 'B', 'A', 'C'], create a sorted list of these keys and then use it to
# print the dictionary items in key order.
# my_dict = {'D': 4, 'B':2, 'A':1, 'C':3}
# keys = ['D', 'B', 'A', 'C']
# sorted_keys = sorted(keys)
# for key in sorted_keys:
#     print(my_dict[key])
#
# #Experiment with sorting a list of tuples of varying lengths, e.g., tuples = [(1, 2), (1,), (1, 2, 3)]. Sort and
# observe the order.
# tuples = [(1, 2), (1,), (1, 2, 3)]
# print((sorted(tuples)))
#
# # Sort the list words = ['arc', 'bat', 'cape', 'ants', 'cap'] in reverse alphabetical order.
# words = ['arc', 'bat', 'cape', 'ants', 'cap']
# print(sorted(words, reverse=True))
#
# #Write a custom key function to sort a list of strings by their last character.
#
# def last_char(word):
#     return word[-1]
#
# print(sorted(words, key=last_char))
#
# """
# Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate
# the list.
#
# # Expected result
# # [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# # [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
# """
# lst = [10, 9, -6, 11, 7, -16, 50, 8]
#
# print(sorted(lst))
# print(sorted(lst, reverse = True))
#
# """
# Repeat the previous exercise but, this time, perform the sort by mutating the original list.
# """
#
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
#
# """
# Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the
# returned list should contain numbers, not strings.
#
# Expected resultCopy Code
# [-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
# [9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
# """
#
# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# def int_str(my_list):
#     new_list = []
#     for item in my_list:
#         item = str(item)
#         new_list.append(item)
#     return sorted(new_list)
#
# print(sorted(int_str(lst)))
# print(sorted(int_str(lst), reverse=True))
#
# """
# How would you sort the following list of dictionaries based on the year of publication of each book, from the
# earliest to the most recent?
#
# books = [
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967',
#     },
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800',
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869',
#     },
# ]
# """
# books = [
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967',
#     },
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800',
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869',
#     },
# ]
#
# def sort_year(my_list):
#     return int(my_list["published"])
#
# print(sorted(books, key = sort_year))
#
# # Practice Problems: Nested Data Structures
#
# """
# For each object shown below, demonstrate how you would access the letter g.
# """
# lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
# print(lst1[2][1][3])
#
# lst2 = [
#     {
#         'first': ['a', 'b', 'c'],
#         'second': ['d', 'e', 'f']
#     },
#     {
#         'third': ['g', 'h', 'i']
#     }
# ]
#
# print(lst2[1]["third"][0])
#
# lst3 = [['abc'], ['def'], {'third': ['ghi']}]
#
# print(lst3[2]["third"][0][0])
#
# dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
#
# print(dict1['b'][1])
#
# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
# dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
#
# print(list(dict2['3rd'].keys())[0])
#
# # For each of these collection objects, demonstrate how you would change the value 3 to 4.
#
# lst1 = [1, [2, 3], 4]
#
# lst1[1][1] = 4
# print(lst1)
#
# lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
#
# lst2[2] = 4
# print(lst2)
#
# dict1 = {'first': [1, 2, [3]]}
#
# dict1['first'][2][0] = 4
# print(dict1)
#
# dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
# dict2["a"]["b"] = 4
# print(dict2)
#
# #Given the following code, what will the final values of a and b be? Try to answer without running the code.
#
# a = 2
# b = [5, 8]
# lst = [a, b]
#
# lst[0] += 2
# lst[1][0] -= a
# print(lst)
# # [4, [3,8]
#
# """
# One of the most frequently used real-world string operations is that of "string substitution," where we take a
# hard-coded string and modify it with various parameters from our program.
#
# Given the object shown below, print the name, age, and gender of each family member.
#
# Each output line should follow this pattern:
#
#
# (name) is a (age)-year-old (male or female).
# """
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
#
# for key, value in munsters.items():
#     print(f"{key} is a {munsters[key]['age']}-year-old {munsters[key]['gender']}")
#
# """
# Consider the following nested dictionary:
#
# Copy Code
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# Compute and display the total age of the family's male members. Try working out the answer two ways: first with an
# ordinary loop, then with a comprehension.
#
# The result should be 444.
# """
# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }
# #
# total_age = 0
# for member in munsters.values():
#     if member['gender'] == 'male':
#         total_age += member['age']
#
# total_age = {member['age'] for member in munsters.values() if member['gender'] == 'male'}
# print(sum(total_age))

"""
Given the following data structure, return a new list with the same structure, but with the values in each sublist
ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)

Copy Code
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
"""
# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
#
# new_lst = [sorted(item) for item in lst]
# print(new_lst)

"""
Given the following data structure, return a new list with the same structure, but with the values in each sublist
ordered in ascending order as strings (that is, the numbers should be treated as strings). Use a comprehension if you 
can. (Try using a for loop first.)


lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
Expected result
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
"""

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# new_list = [sorted(sublist, key=str) for sublist in lst]
# print(new_list)


"""
Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers 
that they contain. You shouldn't mutate the original list.

Copy Code
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third 
sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:

Expected resultCopy Code
[[1, 8, 3], [1, 6, 7], [1, 5, 3]]
Try to use a comprehension in your solution.
"""

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
#
# def sum_odds(sublist):
#     odd_numbers = [num for num in sublist if num % 2 != 0]
#     return sum(odd_numbers)
#
# new_list = sorted(lst, key=sum_odds)
# print(new_list)


"""
Given the following data structure, return a new list identical in structure to the original but, with each number 
incremented by 1. Do not modify the original data structure. Use a comprehension.


lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
Expected result
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
"""
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
#
# new_list = [ {key: value + 1 for key, value in item.items()} for item in lst]
# print(new_list)


"""
Given the following data structure return a new list identical in structure to the original, but containing only the 
numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
The returned list should look like this:

Expected resultCopy Code
[[], [3, 12], [9], [15, 18]]
Try to use a comprehension for this. However, we recommend first trying it without comprehensions.
"""
#
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
#
# def multiples(my_list):
#     new_list = [num for num in my_list if num % 3 == 0]
#     return new_list
#
# new_lst = [multiples(sublist) for sublist in lst]
# print(new_lst)

"""
Given the following data structure, write some code to return a list that contains the colors of the fruits and the
sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
The return value should look like this:

Expected result
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
"""
#
# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }
#
#
# def transform_item(item):
#     if item['type'] == 'fruit':
#         return [color.capitalize() for color in item['colors']]
#     else:
#         return item['size'].upper()
#
# result = [transform_item(item) for item in dict1.values()]
# print(result)

"""
This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can 
look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the 
numbers are even.


lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
Expected result
[{'e': [8], 'f': [6, 10]}]
"""
#
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]
#
#
# def all_even(dictionary):
#     for values in dictionary.values():
#         if not all([num % 2 == 0 for num in values]):
#             return False
#
#     return True
#
# result = [val for val in lst if all_even(val)]
# print(result)


"""
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, even when some of t
hose items were created on a different server or by a different application. That is, without any synchronization, two 
or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each 
other's toes. It accomplishes this feat through massive randomization. The number of possible UUID values is 
approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with 
such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value 
is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed. There are several UUID versions, 
each with some non-random characteristics in some of the bits. These different versions can play a part in certain 
applications.

Write a function that takes no arguments and returns a string that contains a UUID.
"""
# import random
#
# def random_chars(my_range):
#     char_lst = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     new_chars = []
#     for n in range(1, my_range):
#         new_chars.append(random.choice(char_lst))
#     return new_chars
#
#
# def uuid_gen():
#     eight = random_chars(9)
#     four1 = random_chars(5)
#     four2 = random_chars(5)
#     four3 = random_chars(5)
#     twelve = random_chars(13)
#
#     return f"{''.join(eight)}-{''.join(four1)}-{''.join(four2)}-{''.join(four3)}-{''.join(twelve)}"
#
# def generate_uuid():
#     hex_chars = '0123456789abcdef'
#     sections = [8, 4, 4, 4, 12]
#     uuid = []
#
#     for section in sections:
#         chars = [random.choice(hex_chars) for _ in range(section)]
#         uuid.append(''.join(chars))
#
#     return '-'.join(uuid)
#
# print(uuid_gen())

"""
The following dictionary has list values that contains strings. Write some code to create a list of every vowel 
(a, e, i, o, u) that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
Start by trying to write this using nested loops.

Extra Challenge: Once your nested loop code works, try to refactor the code so it uses a single list comprehension. 
(You can print the resulting list outside of the comprehension.)
"""
# dict1 = {
#     'first':  ['the', 'quick'],
#     'second': ['brown', 'fox'],
#     'third':  ['jumped'],
#     'fourth': ['over', 'the', 'lazy', 'dog'],
# }
#
#
# vowels = "aeiou"
# vowels_in_str = []
#
# for key in dict1:
#     for word in dict1[key]:
#         for char in word:
#             if char in vowels:
#                 vowels_in_str.append(char)
#
# vowels_in_str = [char for key in dict1
#               for word in dict1[key]
#               for char in word if char in vowels]
#
# print(vowels_in_str)

