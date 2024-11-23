# 1

# def ask_number():
#     counter = 0
#     num_list = []
#     while counter < 5:
#         num_list.append(input('Please provide a number greater than zero: '))
#         counter += 1
#     last_num = input("Please enter the last number: ")
#     if last_num in num_list:
#         print(f'{last_num} is in {num_list}')
#     else:
#         print(f'{last_num} is not in {num_list}')
    

# 2 

'''
P: 
Given a string, return true if the string is a palindrom and false otherwise
Input: String
Output: Boolean
- A palindrome reads the same backwards and forwards e.g: madam.
- Case matters in this problem: Madam != madam
- Space counts: 123 21 != 12321
- All inputs will be strings

E: 

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

D:
String

A:
- Given a string, compare the string provided with the reversed version
of it. If they are the same, return true, if not, return false. 

- initiate a reversed_string variable to an empty string
- compare the input with the reversed version
- return true if they are the same and false if they are not

'''

# def is_palindrome(string):

#     return True if string == string[::-1] else False




# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

#3

'''
P: 
Given a string, return true if the string is a palindrom and false otherwise
Input: String
Output: Boolean
- A palindrome reads the same backwards and forwards e.g: madam.
- Case does not matter in this problem: Madam == madam
- Any non-alphanumeric characters should be ignored: 123 21 == 12321
- All inputs will be strings

E: 

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

D:
String

A:
- Given a string, compare the string provided with the reversed version
of it. If they are the same, return true, if not, return false. 

- initiate a reversed_string variable to an empty string
- set the input to lowercase
- remove non alpha-numeric chars
- compare the input with the reversed version
- return true if they are the same and false if they are not

'''

# def is_real_palindrome(string):
#     char_list = []
#     for c in string:
#         if c.isalnum():
#             char_list.append(c)
#     new_string = ''.join(char_list).lower()

#     return True if new_string == new_string[::-1] else False
    


# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

#4

'''
P
Given a list of integers, return another list with the same number of elements
but each element is the running total of the list - each element is the sum of
the previous elements in the list. 

input: List of integers
output: List of integers

- The input list will consist of integers only
- there can be a list with only one element
- the list can be empty

E
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

D
List of integer

A
- initiate a variable sum to zero
- initiate an empty list
- loop through the lists elements
- for each element in the list, add it to Sum
- apend sum to a new list
- return the new list

'''

def running_total(my_list):
    new_list = []
    sum = 0
    for num in my_list:
        sum += num
        new_list.append(sum)
    return new_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True