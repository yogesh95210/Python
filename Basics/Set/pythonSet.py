
# A set is a collection which is unordered, unchangeable*, and unindexed.

#* Note: Set items are unchangeable, but you can remove items and add new items.

# create a set

MySet= {1,2,3}
MySet2= {"a","b","c","d"}
MySet3= {1,2,1,2,3}

print(MySet)  
print(MySet2)  # due to Unordered , canreturn any order   {'b', 'c', 'a', 'd'} /// {'a', 'b', 'd', 'c'}
print(MySet3)  # Return {1, 2, 3}


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}   # true will consider 1. Duplicate not allowed so return {false,true}

print(set1)
print(set2)
print(set3)


set4 = {"abc", 34, True, 40, "male"}
print(set4)



# Access set Items

# with for loop

setData= {1,2,3,4,5,6,7}
for x in setData:
    print(x)

# check data is in set data

thisSet= {1,2,3,4}
print(2 in thisSet) # True
print(8 in thisSet) # false

# check data is not in set data


thisSet= {1,2,3,4}
print(2 not in thisSet)  # False
print(8 not in thisSet)  #True


# Note :-- Once a set is created, you cannot change its items, but you can add new items.

# Add Items in set data type
# add() Method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)  # return {'cherry', 'banana', 'orange', 'apple'}  // every time code runs order can be changed of result

# update() method

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)  # return {'apple', 'cherry', 'banana', 'pineapple', 'papaya', 'mango'}

# we can add any itreable in set data

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# To remove items from set we have remove() and discard() Method
# remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# discard() method

# Note --->  Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# pop() method
# a randome item can be pop (every time when code compile gives new result)
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear() method to emplty the set

set= {1,2,3,4}
set.clear()
print(set)  # set()

# del will delete entire set and throws error




