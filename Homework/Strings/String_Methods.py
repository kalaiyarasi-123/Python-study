#uppercase

s1="wellcome show data"
print(s1.upper())

#Lowercase

s1="METHODS"
print(s1.lower())

#The capitalize() method in Python is used to change the first letter of a string to uppercase
s = "hello WORLD"
res = s.capitalize()
print(res)

#title() method used  to convert first letter of each word is capitalized and all other letters are lowercase.

a = "hello geek"

# Converts string to title case
b = a.title()  
print(b)

# string swapcase() Method

#swapcase() method is used all the uppercase characters  converted to lowercase, and all the lowercase characters are converted to uppercase.
s = "I love Python"

swapped_text = s.swapcase()
print(swapped_text)

#strip()The strip() method removes any whitespace from the beginning or the end
s = "   Hello World!   "
print(s.strip())

#The replace() method replaces a string with another string:

s1 = "I love programming"
s2 = s1.replace("programming", "wellcom")
print(s2)

#Concatenating Strings Joining two or more strings together
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#Python String join() Method

#we use join() method to combine a list of strings into a single string with each string separated by a space.

a = ['Hello', 'world', 'from', 'Python']
res = ' '.join(a)
print(res)

#String index() Method

s = "Python programming"

p = s.index("prog")
print(p)

#Python String find() Method
#ifnd() method  returns the index of the first occurrence
s = "Welcome to Geek Python programming Geek"
index = s.find("Geek")
print(index) 

#If the given string is not found, it returns -1.
s = "Welcome to GeekforGeeks!"
index = s.find("programming")
print(index)

#String count() Method
#Return the number of times the given string appears in the string:
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

my_string = "Hello, world!"
del my_string
print(my_string)
# my_string is no longer accessible