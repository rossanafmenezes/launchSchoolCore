# Question 1 
# It will raise an index error becaus eyou are trying to add an element to a 
# position that is out of range

# Question 2

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation(string):
    if string[-1] == '!':
        return True
    else:
        return False
    

print(exclamation(str1))
print(exclamation(str2))

print(str1.endswith('!'))
print(str2.endswith('!'))

# Question 3

famous_words = "seven years ago..."

new_sentence = "Four score and " + famous_words
new_sentence2 = f"Four score and {famous_words}"

print(new_sentence)
print(new_sentence2)

# Question 4 
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

print(munsters_description.capitalize())

# Question 5

munsters_description = "The Munsters are creepy and spooky."

print(munsters_description.swapcase())



# Question 6

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print('Dino' in str1)
print('Dino' in str2)

#Question 7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones[-1] = "Dino"
# flintstones.append("Dino")
print(flintstones)

# Question 8

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)

# Question 9

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as '

words = advice.split(" ")
print(words)
new_advice = words[0:8]
print(" ".join(new_advice))

# advise.split('house)[0]
#print(advise)

# Question 10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))



