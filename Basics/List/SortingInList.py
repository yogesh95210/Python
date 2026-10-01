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
