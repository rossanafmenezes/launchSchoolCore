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

# def running_total(my_list):
#     new_list = []
#     sum = 0
#     for num in my_list:
#         sum += num
#         new_list.append(sum)
#     return new_list

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True


'''
P
Given a string that can have zero or more space separated words, return a 
dictionay that counts the words based on word lenght. 

E
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

D
List
Dictionary

A
Given a string, split the string into a list with all the word, then loop through the list
getting the length for each word. If the length is already part of the dictionary, increase
the count for that length. If not, add a new key-value pair where the length is the key and the count
of 1 is the value. 

- initiate an empty dict
- initiate a list that holds each separate word of the string being passed into the
function as the argument
- loop through the list
- for every word in the list, add the word length to a key of the dict and the counter + 1 to the value
return the dict

'''

# def word_sizes(string):
#     word_size ={}
#     word_list = string.split()
#     for word in word_list:
#         size = len(word)
#         if size not in word_size:
#             word_size[size] = 0
#         word_size[size] += 1

#     return word_size


# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

#5

'''
Same as before but remove non-letter characters
'''

# def word_sizes(string):
#     word_size ={}
#     word_list = string.split()
#     for word in word_list:
#         word = letters_only(word)
#         size = len(word)
#         if size not in word_size:
#             word_size[size] = 0
#         word_size[size] += 1

#     return word_size

# def letters_only(string):
#     char_list = []
#     new_string = ""
#     for c in string:
#         if c.isalpha():
#             char_list.append(c)
#     new_string = "".join(char_list)
#     return new_string

# string = "What's up doc?"
# print(word_sizes(string)) == {6: 1, 2: 1, 4: 1}


'''
P 
Given a string, create a function that will swap the first and the last letter of
each word in the string, so hello becomes oellh. 

input: string
output: string with swaped letters

E

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

D
List - hold words in the string
String - return the new string with first and last chars swaped

A
Loop through each word of a given string, swap the first and last letter of each word, 
return the new string

initiate a list that will contain the words of the string as separate elements
loop through the list of words
initiate a new empty list
for every word, swap the first and last charaters
apend the new word to the new list
join the words in the new list into a new string
return a new string
'''

#6 

# def swap(string):
#     words = string.split()
#     new_words = []
#     for word in words:
#         if len(word) == 1:
#             new_words.append(word)
#         else:
#             new_words.append(word[-1] + word[1:-1] + word[0])
#     return ' '.join(new_words)



# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True
# print(swap('Oh what a wonderful day it is'))


'''
P
Take a string of numeric digits and turn into integers

input: string
output: Integer

- All numbers are positive
- all character in the string are numeric
- there will be no empty strings
- built-in Python functions cannot be used

E

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

D

Lists

A


'''

#7

# def string_to_integer(string):
#     int_dict = {
#         "0" : 0,
#         "1" : 1, 
#         "2" : 2,
#         "3" : 3, 
#         "4" : 4, 
#         "5" : 5, 
#         "6" : 6, 
#         "7" : 7, 
#         "8" : 8, 
#         "9" : 9, 
#     }

#     rev_string = string[::-1]
#     multiplier = 1
#     new_int = 0
#     for c in rev_string:
#         number = int_dict[c] * multiplier
#         new_int += number
#         multiplier *= 10

#     return new_int

# def string_to_integer(string):
#     int_dict = {
#         "0" : 0,
#         "1" : 1, 
#         "2" : 2,
#         "3" : 3, 
#         "4" : 4, 
#         "5" : 5, 
#         "6" : 6, 
#         "7" : 7, 
#         "8" : 8, 
#         "9" : 9, 
#     }

#     new_int = 0
#     for c in string:
#         new_int = (10 * new_int) + int_dict[c]

#     return new_int


# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True


# def string_to_signed_integer(string):
#     int_dict = {
#         "-" : 0,
#         "+" : 0,
#         "0" : 0,
#         "1" : 1, 
#         "2" : 2,
#         "3" : 3, 
#         "4" : 4, 
#         "5" : 5, 
#         "6" : 6, 
#         "7" : 7, 
#         "8" : 8, 
#         "9" : 9, 
#     }

#     new_int = 0
#     for c in string:
#         new_int = (10 * new_int) + int_dict[c]
    
#     if string[0] == '-':
#         new_int *= -1

#     return new_int

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

''' 
P
Take an integer and convert it to a string

input: Integer
output: String

- All numbers are positive
- there will be no negative numbers
- built-in Python functions cannot be used

E

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

D

Dictionary

A

'''

# def integer_to_string(number):
#     new_string = ""
#     string_dict = {
#         0 : "0",
#         1 : "1", 
#         2 : "2",
#         3 : "3", 
#         4 : "4", 
#         5 : "5", 
#         6 : "6", 
#         7 : "7", 
#         8 : "8", 
#         9 : "9", 
#     }

#     if number == 0:
#         new_string = string_dict[0]
#     else:
#         while number > 0:
#             digit = number % 10
#             new_string = string_dict[digit] + new_string
#             number //= 10
#     return new_string    

    


# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

''' 
P
Take a signed integer and convert it to a string

input: Integer
output: String

- Numbers are positive or negative
- built-in Python functions cannot be used

E

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

D

Dictionary

A

'''

# def signed_integer_to_string(number):
#     new_string = ""
#     if number > 0:
#         new_string = '+' + integer_to_string(number)
#     elif number < 0:
#         new_string = '-' + integer_to_string(-number)
#     return new_string if new_string else '0'


# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True

