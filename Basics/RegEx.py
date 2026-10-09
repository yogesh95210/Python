import re

text= "The rain in Spain"
print(len(text))
x = re.search("^The.*Spain$", text)  ##Check if the string starts with "The" and ends with "Spain":
print(x)  #<re.Match object; span=(0, 17), match='The rain in Spain'>

if x:
  print("YES! We have a match!")
else:
  print("No match")




# findall()  method

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # ["ai","ai"]
print(type(x))  # list

# search method


txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

y = re.search("Portugal", txt)
print(y)


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


# split() method

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#sub() method


txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
