#1 Cute Angles
"""
- Problem:
Convert a given angle provided in either int or float and convert it to degrees, minutes, and seconds returning a string formatted as D°M'S".
The angle provided will be between 0 and 360 degrees.
You need to append the degree symbol (°) to the degrees, a single quote (') to the minutes, and a double quote (") to the seconds.

- Examples:
dms(30)       # 30°0'0"
dms(76.73)    # 76°43'48"
dms(254.6)    # 254°36'0"

- Data Structure:
Use division and modulo operations to extract degrees, minutes, and seconds from the input angle.

- Algorithm:
1. Define a function `dms` that takes a single argument `angle`.
2. Extract the degrees by taking the integer part of the angle.
3. Calculate the minutes by taking the decimal part of the angle, multiplying it by 60, and taking the integer part of the result.
4. Calculate the seconds by taking the decimal part of the minutes, multiplying it by 60, and rounding the result to the nearest integer.
5. Format the result as a string in the format "D°M'S"" and return it.

"""

# Solution without using built-in functions

# def integer_to_string(number):
#     new_string = ""
#     digits = {
#             0.0 : "0",
#             1.0 : "1",
#             2.0 : "2",
#             3.0 : "3",
#             4.0 : "4",
#             5.0 : "5",
#             6.0 : "6",
#             7.0 : "7",
#             8.0 : "8",
#             9.0 : "9",
#         }
#     while number > 0:
#         digit = number % 10
#         new_string = digits[digit] + new_string
#         number //= 10
#     return new_string if new_string else digits[0]

# def dms(angle):
#     degree = integer_to_string(angle - (angle % 1))
#     minutes_f = (angle % 1) * 60
#     if minutes_f < 10:
#         minutes = f"0{integer_to_string(minutes_f - (minutes_f % 1))}"
#     else:
#         minutes = integer_to_string(minutes_f - (minutes_f % 1))
#     seconds_f = (minutes_f % 1) * 60
#     if seconds_f < 10:
#         seconds = f"0{integer_to_string(seconds_f - (seconds_f % 1))}"
#     else:
#         seconds = integer_to_string(seconds_f - (seconds_f % 1))
#
#     return f"{degree}{DEGREE}{minutes}'{seconds}\""

# def dms(angle):
#     degree = int(angle)
#     minutes = (angle % 1) * 60
#     seconds = int((minutes % 1) * 60)
#
#
#     return f"{str(degree)}{DEGREE}{int(minutes):02d}'{seconds:02d}\""
# DEGREE = "\u00b0"

# Solution using built-in functions
#
# def dms(angle):
#     degree = int(angle)
#     minutes_f = (angle % 1) * 60
#     if minutes_f < 10:
#         minutes = f"0{int(minutes_f - (minutes_f % 1))}"
#     else:
#         minutes = int(minutes_f - (minutes_f % 1))
#     seconds_f = (minutes_f % 1) * 60
#     if seconds_f < 10:
#         seconds = f"0{int(seconds_f - (seconds_f % 1))}"
#     else:
#         seconds = int(seconds_f - (seconds_f % 1))
#
#     return f"{degree}{DEGREE}{minutes}'{seconds}\""
"""
2 Combining Lists
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two
lists. You may assume that both arguments will always be lists.

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
"""

# def union(list1, list2):
#     return set(list1 + list2)
#
# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

"""
3 Halvsies
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. 
Put the first half of the original list elements in the first element of the return value and put the second half in the
second element. If the original list contains an odd number of elements, place the middle element in the first half list.

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
"""

# def halvsies(my_list):
#     mid_point = (len(my_list) + 1) // 2
#     list1 = my_list[:mid_point]
#     list2 = my_list[mid_point:]
#     new_list = [list1, list2]
#     return new_list
#
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

"""
4 Find the Duplicate

Given an unordered list and the information that exactly one value in the list occurs twice (every other value occurs 
exactly once), determine which value occurs twice. Write a function that finds and returns the duplicate value.

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
"""

# def find_dup(my_list):
#     new_list = []
#     for item in my_list:
#         if item in new_list:
#             return item
#         else:
#             new_list.append(item)
#
# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

"""
5 Combine Two Lists

Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
"""

# def interleave(list1, list2):
#     new_list = []
#     for a, b in zip(list1, list2):
#         new_list.extend([a, b])
#     return new_list
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True

"""
6 - Multiplicative Average

Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the 
result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal 
places.

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
"""

# def multiplicative_average(my_list):
#     result = 1
#     for item in my_list:
#         result *= item
#     return "{:.3f}".format(result / len(my_list))
#
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

"""
7 Multiply Lists
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains
 the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments 
 contain the same number of elements.
 
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

"""

# def multiply_list(list1, list2):
#     final_list = []
#     for a, b in zip(list1, list2):
#         result = a * b
#         final_list.append(result)
#     return final_list

#   return [a * b for a, b in zip(list1, list2)]

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

"""
8 List of Digits

Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

"""
#
# def digit_list(number):
#     return [int(item) for item in str(number)]
#
# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True

"""
9 How Many?

Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element
alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
"""

# def count_occurrences(my_list):
#     occurrences = {}
#
#     for item in my_list:
#         occurrences[item] = occurrences.get(item, 0) + 1
#     #     if item not in occurrences:
#     #         occurrences[item] = 1
#     #     else:
#     #         occurrences[item] += 1
#     for a, b in occurrences.items():
#         print(
#             f"{a} => {b}"
#         )
#
#
# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

"""
10 List Average
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, 
rounded down to the integer component of the average. The list will never be empty, and the numbers will always be 
positive integers.


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
"""
#
# def average(my_list):
#     return sum(my_list) // len(my_list)
#
# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True