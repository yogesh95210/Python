# List 

x= [1,2,3,4,5,6,7,8,9]

# Accesing list item
# Positive Index  
print(x[2])  # return 3
print(x[7])  # return 8


# Negative Index
print(x[-1])  # return 9
print(x[-5])  # return 5

# Length of list

print(len(x))

# we can include list item any data type

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


#range of indexes

print(x[2:5])  # [3,4,5]
print(x[2:])   # [3,4,5,6,7,8,9]
print(x[:4])   # [1,2,3,4]

# range of negative indexes

print(x[-4:-1])  # [6,7,8]


# change List Item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # ['apple', 'watermelon']
  
# Above given range toh delete hogi and then replacement hoga

# insert Item in List  at specific index

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   # ['apple', 'banana', 'watermelon', 'cherry']

# Insert item at the end of list

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ["apple", "banana", "cherry","orange"]

# Extent List from another list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Remove item in list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# remove only first occurence

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# remove specfic index

a= [1,2,3,4,5]
a.pop(2)
print(a) # [1,2,4,5]

# remove last item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) 

# del keyword with list

thislist = ["apple", "banana", "cherry"]
del thislist  # delete the entire list

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)  # del the item at given index

# clear the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

