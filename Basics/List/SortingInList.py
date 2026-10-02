a = ["orange", "mango", "kiwi", "pineapple", "banana"]
a.sort()
print(a)


b= [6,2,10]

b.sort()
print(b)

c= [True,False,True]
c.sort()
print(c)

#Mixed Types: Strings + Numbers (Throws an Error)

#mixed_list = ["orange", 1, "mango"]
#mixed_list.sort() 
# TypeError: '<' not supported between instances of 'int' and 'str'


#Mixed Strings: Strings containing Letters + Numbers
alphanumeric_strings = ["apple", "10", "2", "banana"]
alphanumeric_strings.sort()

print(alphanumeric_strings)
# Output: ['10', '2', 'apple', 'banana']


#Mixed Numbers: Numbers + Booleans (Works)

mixed_bool_num = [1, True, False, 0]
mixed_bool_num.sort()

print(mixed_bool_num)
# Output: [False, 0, 1, True]  (Keeps original relative order for equivalents)


#How to fix it: Sorting everything as a single type

mixed_list = ["orange", 1, "mango", 10]

# Convert everything to a string just for comparison purposes
mixed_list.sort(key=str)

print(mixed_list)
# Output: [1, 10, 'mango', 'orange'] (Sorted according to string rules)





# Sort Decending

c = ["orange", "mango", "kiwi", "pineapple", "banana"]
c.sort(reverse = True)
print(c)


list = [100, 50, 65, 82, 23]
list.sort(reverse = True)
print(list)   # [100, 82, 65, 50, 23]


# Case Insensitive Sort

arr= ["banana", "Orange", "Kiwi", "cherry"]
arr.sort()
print(arr)   #['Kiwi', 'Orange', 'banana', 'cherry']   # first capital letter word sort then small letter word

# 

arrlist = ["banana", "Orange", "Kiwi", "cherry"]
arrlist.sort(key = str.lower)
print(arrlist)   #['banana', 'cherry', 'Kiwi', 'Orange']  # first small letter word sort then capital letter sort


# Reverse letter

array = ["banana", "Orange", "Kiwi", "cherry"]
array.reverse()
print(array)   # 