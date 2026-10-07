# Range in Python
# syntex  == range(start,stop,step)
x= range(10)
y= range(1,10)
z= range(1,10,2)
print(x, type(x)) #range(0, 10) <class 'range'>
print(x, type(y)) #range(0, 10) <class 'range'>
print(x, type(z)) #range(0, 10) <class 'range'>

print(list(x))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
print(list(y))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(z))  #[1, 3, 5, 7, 9]

# length of range

r = range(0, 10, 2)
print(len(r))

# Membership Testing

r = range(0, 10, 2)
print(6 in r)  # True
print(7 in r)  # False

# Slicing Range 

r = range(10)
print(r[2]) # 2
print(r[:3]) # range(0,3)
