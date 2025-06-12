#b = "Hello, World!"
#print(b[2:5])

#slicing  from the start  
#b = "welcome, besant!"
#print(b[:7])

"""a="Troll Geek"
print(a[0:5])

s = "Hello, Python!"
print(s[0:5])"""

#slicing from the end
#b = "Hello, World!"
#print(b[2:])

#Example 2: Get All Characters Before or After a Specific Position
#s = "Hello, World!"

# Characters from index 7 to the end
#print(s[7:])

# Characters from the start up to index 5 (exclusive)
#print(s[:5])

#Example 3: slice Characters Between Two Positions
#s = "Hello, World!"
# Characters from index 1 to index 5 (excluding 5)
#print(s[1:5])

#Example4:how to get the All character from the string
#s = "Hello, World!"

# Get the entire string
"""s2 = s[:]
s3 = s[::]

print(s2)
print(s3)"""

#m = "abcdefghi"

# Every second character
#print(m[::2])


#Using Negative Indexing in Slicing

s = "hello, world"

#print(s[-4:])
#print(s[:-3])

print(s[-5:-2])

#Reverse a String Using Slicing
s = "Python"

# Reverse the string
print(s[::-1])