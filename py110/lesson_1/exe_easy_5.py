def bla():
    pass

"""
1 - Inverting Dictionary
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its 
values become keys.

Example

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
"""

# def invert_dict(my_dict):
#     new_dict = {}
#     for key, value in my_dict.items():
#         new_dict[value] = key
#     return new_dict
#
# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

"""
2 - Retain Specific Keys
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the 
specified keys.

Example
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True
"""

# def keep_keys(my_dict, keys_lst):
#     return {key: value for key, value in my_dict.items() if key in keys_lst}
#
# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }
#
# keys = ['red', 'blue']
#
# print(keep_keys(input_dict, keys))

"""
3 - Delete Vowels
Write a function that takes a list of strings and returns a list of the same string values, but with all 
vowels (a, e, i, o, u) removed.

Examples
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
"""

# VOWELS = "aeiouAEIOU"
#
# def strip_vowels(string):
#     return "".join(c for c in string if c not in VOWELS)
#
# def remove_vowels(string_list):
#     return [strip_vowels(word) for word in string_list]

# Works but I'll try a refactored version above

# def remove_vowels(str_lst):
#     new_list = []
#
#     for word in str_lst:
#         char_list = []
#         for c in word:
#             if c not in VOWELS:
#                 char_list.append(c)
#         new_word = ''.join(char_list)
#         new_list.append(new_word)
#     return new_list
#
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True
#
# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True
#
# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

"""
4 -How Long Are You?
Write a function that takes a string as an argument and returns a list that contains every word from the string, with 
each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the 
function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.

Examples
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True
"""

# def string_to_list(string=""):
#     return string.split()
#
# def word_lengths(string= ""):
#     return [f"{word} {len(word)}" for word in string_to_list(string)]
#
#
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True
#
# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True
#
# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True
#
# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True
#
# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

"""
5 - List Element Multiplication
Given two lists of integers of the same length, return a new list where each element is the product of the corresponding 
elements from the two lists.

Example
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
"""

# def multiply_items(lst_a, lst_b):
#     return [lst_a[idx] * lst_b[idx] for idx in range(len(lst_a))]
#
# # another option:
# # def multiply_items(lst_a, lst_b):
# #     return [a * b for a, b in zip(lst_a, lst_b)]
#
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

"""
6 - Sum of Sums
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. 
Examine the examples to see what we mean. You may assume that the list always contains at least one number.

Examples
print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True
"""

# def slice_list(list_1):
#     return [list_1[:i + 1] for i in range(len(list_1))]
#
# def sum_of_sums(list_2):
#     result = 0
#     for list in  slice_list(list_2):
#         result += sum(list)
#     return result
#
# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21
#
# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
#
# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35
#
# print(sum_of_sums([4]) == 4)                      # True

"""
7 - Sum of Digits
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

Examples
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
"""
#
# def sum_digits(number: int):
#     return sum(int(c) for c in str(number))
#
# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

"""
8 - Staggered Case (Part 1)
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. 
Every other character, starting from the first, should be capitalized and should be followed by a lowercase or 
non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for 
determining when to switch between upper and lower case.

ExamplesCopy Code
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
"""

# def staggered_case(string):
#     new_str = ''
#     for idx, char in enumerate(string):
#         if idx % 2 == 0:
#             new_str += char.upper()
#         else:
#             new_str += char.lower()
#     return new_str
#
# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True
#
# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True
#
# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True
#
# print(staggered_case('') == "")          # True

"""
9 - Staggered Case (Part 2)
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it 
should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; 
they just don't count when toggling the desired case.

ExamplesCopy Code
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
"""

# def staggered_case(string):
#     new_string = ''
#     upper = True
#     for char in string:
#         if char.isalpha():
#             new_string += char.upper() if upper else char.lower()
#             upper = not upper
#         else:
#             new_string += char
#     return new_string
#
#
# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True
#
# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True
#
# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True
#
# print(staggered_case('') == "")          # True
#
# """
# 10 - Remove Consecutive Duplicates
# Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial
# occurrence. Return the refined sequence.
#
# ExampleCopy Code
# original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True
# """
# def unique_sequence(sequence):
#     new_sequence = []
#     for n in sequence:
#         if not new_sequence or n != new_sequence[-1]:
#             new_sequence.append(n)
#     return new_sequence
#
# original = [1, 6, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
# expected = [1, 6, 1, 2, 6, 5, 3, 4]
# print(unique_sequence(original) == expected)      # True