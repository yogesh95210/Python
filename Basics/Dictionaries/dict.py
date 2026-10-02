
# Key : Value pair stores /// like a object

# create an dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Ordered or Unordered?
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

#Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020   # same key not allowed
}
print(thisdict)  ## will give result and takes last key in result

# Access of item in dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# we have another method as well too, get() method

y= thisdict.get("year")
print(y)


# to get keys()

print(thisdict.keys())  # dict_keys(['brand', 'model', 'year'])

# to get values()

print(thisdict.values()) # dict_values(['Ford', 'Mustang', 1964])


# To change values we have two ways

d1= {
    1: "one",
    2: "two",
    3: "three"
}

d1[2]= "2"    # we can add items in this way like 4: "four" 

print(d1)

d2={
    1: "one",
    2: "two",
    3: "three"
}
d2.update({3:"3"})
print(d2)

d3 ={
    1: "one",
    2: "two",
    3: "three"
}

d3.update({4: "four"})   # we can add items with update method
print(d3)