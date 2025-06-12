#Find Length of String in Python
#HY1000110054

s1 = "abcd"
print(len(s1))

s2 = ""
print(len(s2))

s3 = "a"
print(len(s3))

#Example 1: Len() function with tuples and List
# with tuple
tup = (1,2,3)
print(len(tup))

# with list
l = [1,2,3,4]
print(len(l))

#Example 2: Python len() TypeError
print(len(True))

#Example 3: Python len() with dictionaries and sets
dic = {'a':1, 'b': 2}
print(len(dic))

s = { 1, 2, 3, 4}
print(len(s))

#Example 5: Python len() with range()
l=range(1,10)
print(len(l))