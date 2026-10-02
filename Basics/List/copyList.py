# make copy with copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # ['apple', 'banana', 'cherry']

# make copy with list() method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # ['apple', 'banana', 'cherry']

# Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)  # ['apple', 'banana', 'cherry']