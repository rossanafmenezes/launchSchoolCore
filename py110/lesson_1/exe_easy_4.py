def a():
    pass
"""
1 -Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on 
the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, 
seventeen, eighteen, nineteen

Example
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
"""
# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# def word_for_number(num):
#     num_to_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
#                     9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
#                     16: 'sixteen',
#                     17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
#     return num_to_words[num]

# def number_for_word(word):
#     words_to_nums = {
#     'zero': 0,
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'six': 6,
#     'seven': 7,
#     'eight': 8,
#     'nine': 9,
#     'ten': 10,
#     'eleven': 11,
#     'twelve': 12,
#     'thirteen': 13,
#     'fourteen': 14,
#     'fifteen': 15,
#     'sixteen': 16,
#     'seventeen': 17,
#     'eighteen': 18,
#     'nineteen': 19
# }
#     return words_to_nums[word]

# def alphabetic_number_sort(lst):
#     word_lst = []
#     num_lst =[]
#     for item in lst:
#         word_lst.append(word_for_number(item))
#     word_lst = sorted(word_lst)
#     for word in word_lst:
#         num_lst.append(number_for_word(word))
#
#     return num_lst
# WORDS =['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
#      'thirteen', 'fourteen', 'fifteen', 'sixteen',
#      'seventeen', 'eighteen', 'nineteen']
#
# def word_for_number(num):
#     return WORDS[num]
#
# def alphabetic_number_sort(lst):
#     new_lst = sorted(lst, key=word_for_number)
#     return new_lst
#
# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
#
# print(alphabetic_number_sort(input_list) == expected_result)

"""
2 - Merge Sets
Given two lists, convert them to sets and return a new set which is the union of both sets.

Example
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
"""

# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
#
# def merge_sets(lst1, lst2):
#     return set(lst1 + lst2)
#
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})

"""
3 - Immutable Intersection
Transform two lists into frozen sets and find their common elements.

ExampleCopy Code
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
"""
# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
#
# def intersection(lst1, lst2):
#     return frozenset(lst1).intersection(lst2)
#
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

"""
4 - Arrange a Dictionary
Given a dictionary, return its keys sorted by the values associated with each key.

Example
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
"""

#
# def order_by_value(a_dict):
#     return sorted(a_dict, key=a_dict.get)
#
# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
#
# print(order_by_value(my_dict))
# print(order_by_value(my_dict) == keys)  # True

"""
5 - Unique Elements
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

Example
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

"""
# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
#
# def unique_from_first(lst1, lst2):
#     return set(lst1) - set(lst2)
#
# print(unique_from_first(list1, list2))
# print(unique_from_first(list1, list2) == {9, 3})

"""
6 - Leading Substrings
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should 
begin with the first letter of the word, and the list should be ordered from shortest to longest.

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
"""

# def leading_substrings(my_str):
#     return [my_str[:i] for i in range(1, len(my_str) + 1)]
#
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

"""
7 - All Substrings

Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the 
substring begins. This means that all substrings that start at index position 0 should come first, then all substrings 
that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings 
at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

Example
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
"""

# def leading_substrings(my_str):
#      return [my_str[:i] for i in range(1, len(my_str) + 1)]
#
# def substrings(s):
#     result = []
#     for first_char in range(len(s)):
#         sub = s[first_char:]
#         result.extend(leading_substrings(sub))
#     return result
#
# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]
#
# print(substrings('abcde') == expected_result)  # True

"""
8 - Palindromic Substrings
Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist of
a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted 
by their order of appearance in the input string. Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a 
palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

Examples
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

"""

# def leading_substrings(s):
#      return [s[:i] for i in range(1, len(s) + 1)]
#
# def substrings(s):
#     result = []
#     for idx in range(len(s)):
#         sub_string = s[idx:]
#         result.extend(leading_substrings(sub_string))
#     return result
#
# def palindromes(s):
#     substring_lst = substrings(s)
#     return  [word for word in substring_lst if len(word) > 1 and word == word[::-1]]
#
# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True
#
# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True
#
# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

"""
9 - Inventory Item Transactions
Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list 
containing only the transactions for the specified inventory item.

Example
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

"""
# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# def transactions_for(transaction_id, transaction_lst):
#     return [item for item in transaction_lst if item["id"] == transaction_id]
#
# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

"""
10 - Inventory Item Availability
Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item 
(an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The 
function should return True only if the sum of the quantity values of the item's transactions is greater than zero. 
Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's 
quantity.

You may (and should) use the transactions_for function from the previous exercise.

Examples
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
"""

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

def select_items(transaction_id, transaction_lst):
    return [item for item in transaction_lst if item['id'] == transaction_id]

def is_item_available(transaction_id, transaction_lst):
    items_in = 0
    items_out = 0
    items_lst = select_items(transaction_id, transaction_lst)
    for item in items_lst:
        if item['movement'] == 'in':
            items_in += item['quantity']
        elif item['movement'] == 'out':
            items_out += item['quantity']
    return True if items_in - items_out > 0 else False


print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

