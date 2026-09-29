x="Hello!"

print(type(x)) #str

str= """fh hfk egh lwejg lwfjlw ;wjf;k
jhgjgj ejglh jwegjk owgflew pwghlew lwgjle wgle
sdfh wehgk lewjgl lwa lawhgl lwglj lwgjl egnj
"""
print(str)


# strings are Array

str1= "MSDhoni"
# print(str1[2])  # D

#Looping through Strings

for y in str1:
 print(y)


# check string

text= "The best thing about Msdhoni is!"

print("best" in text)
print("Best" in text)

# Length og string

print(len(text))

# with if Statement

txt="The best thing about Msdhoni is!"

if "The" in txt:
 print(True)
 
 # not in statement
 print("about" not in txt)



 # Slicing with Strings

 string= "PYTHON"

#Slicing in given range
print(string[2:5]) # THO

#Slicing from the start

print(string[:5]) #PYTHO

#slicing to the End

print(string[2:])  # THON

# negative indexing slicing

print(string[-5:-2])  # YTHs



