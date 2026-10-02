# Union Method

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# join using | 

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Join multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset1 = set1.union(set2, set3, set4)
myset2 = set1 | set2 | set3 |set4

print(myset1)
print(myset2)

# Join set and Tuple

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# using intersection() method
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set4= set1 & set2  # it will return same result as intersection()
print(set3)  # {"apple"}
print(set4)  # {"apple"}

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# intersection_update() method
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1) # {"apple"}

# difference() method
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set4 = set1- set2  #  return same resule as above
print(set3)  # {"cherry","banana"}
print(set4)  # {"cherry","banana"}


