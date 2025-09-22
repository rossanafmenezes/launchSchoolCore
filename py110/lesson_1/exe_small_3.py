"""
1 After Midnight (Part 1)

The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is
positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm).
Your function should work with any integer input.

You may not use Python's datetime module.


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

Disregard Daylight Savings and Standard Time and other complications.

"""
# MINUTES_PER_DAY = 1440
# MINUTES_PER_HOUR = 60
#
# def time_of_day(minutes):
#     remaining_time = minutes % MINUTES_PER_DAY
#     remaining_hours = remaining_time // MINUTES_PER_HOUR
#     remaining_minutes = remaining_time % MINUTES_PER_HOUR
#
#     return f"{int(remaining_hours):02d}:{int(remaining_minutes):02d}"
#
# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

"""
2 After Midnight (Part 2)

As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is 
before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after 
midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
"""

# def after_midnight(time):
#     return int(time[:2]) * 60 + int(time[3:]) if time != "24:00" else 0
#
# def before_midnight(time):
#     total_minutes = after_midnight(time)
#     return 0 if time == "24:00" or time == "00:00" else 1440 - total_minutes
#
# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

"""
3 Double Char (Part 1)
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

Examples
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

"""

# def repeater(my_string):
#     return "".join(f"{c}{c}" for c in my_string)
#
# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

"""
4 Double Char (Part 2)
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. 
The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
"""

# def double_consonants(my_string):
#     consonants = [
#         "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
#         "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
#         "B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
#         "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"
#     ]
#     # new_string = ""
#     # for c in my_string:
#     #     if c not in consonants:
#     #         new_string += c
#     #     else:
#     #         new_string += c * 2
#     return "".join(c if c not in consonants else c * 2 for c in my_string)
#
# # "".join(c if c in vowels else c * 2 for c in my_string)
#
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

"""
5 Reverse Number

Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

"""

# def reverse_number(number):
#     return int(str(number)[::-1])
#
# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

"""
6 Counting Up

Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

"""

# def sequence(number):
#     return list(range(1, number + 1))
#
# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

"""
7 Name Swapping
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should 
return a new string consisting of the last name, a comma, a space, and the first name.

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

"""

# def swap_name(name):
#     my_list = name.split(" ")
#     return f"{my_list[-1]}, {' '.join(my_list[:-1])}"
#
# print(swap_name('Joe Mike Roberts'))   # True

"""
8 Sequence Count
Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting 
number of a sequence that your function will create. The function should return a list containing the same number of 
elements as the count argument. The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. 
If the count is 0, the function should return an empty list.

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
"""

# def sequence(count, starter):
#     return [starter * n for n in range(1, count +1)]
#
# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

"""
9 Reversed Lists
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed 
into the function. The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
"""
# def reverse_list(my_list):
#     first_idx = 0
#     last_idx = -1
#     while first_idx < len(my_list) /2:
#         my_list[first_idx], my_list[last_idx] = my_list[last_idx], my_list[first_idx]
#         last_idx -=1
#         first_idx += 1
#     return my_list
#
# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True
#
# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True
#
# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True
#
# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

"""
10 Matching Parenthesis?
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly 
balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

ExamplesCopy Code
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

Note that balanced pairs must start with a (, not a ).
"""

# def is_balanced(my_string):
#     my_list =[]
#     for item in my_string:
#         if item == "(" or item == ")":
#             my_list.append(item)
#     print(my_list)
#
# # print(is_balanced("What (is) this?") == True)        # True
# # print(is_balanced("What is) this?") == False)        # True
# # print(is_balanced("What (is this?") == False)        # True
# # print(is_balanced("((What) (is this))?") == True)    # True
# # print(is_balanced("((What)) (is this))?") == False)  # True
# # print(is_balanced("Hey!") == True)                   # True
# # print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up("))      # True

# fs1 = frozenset([1,2,3])
# fs2 = frozenset([3,4,5])
#
# print(fs1 & fs2)