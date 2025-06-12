#Using string slicing

s = "Hello, Wellcome"
rev = s[::-1]
print(rev)

#Using reversed() and join()

s = "wellcome, Besant"
rev = ''.join(reversed(s))
print(rev)

#To reverse the string s = "wellcome, Besant"  but same place
s = "wellcome, Besant"
reversed_words = ' '.join(word[::-1] for word in s.split())
print("rever",reversed_words)

#Using a Loop (manual method)
s = "kalaiyarasi"

# Initialize an empty string to hold reversed result
rev = ""

# Loop through each character in original string
for char in s:
  
    # Add current character to front of reversed string
    rev = char + rev

print(rev)


str= "wellcome, Besant"
reversed_s = ''
for char in str:
    reversed_s = char + reversed_s
print(reversed_s)