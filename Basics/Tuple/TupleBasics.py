# One of the built-in data types in Python
thisTuple= (1,2,3,4,5,6,7,8)

print(thisTuple)

#Tuple are Unchangable and  immutable
# Tuple mein add, remove and update operation karne ke liye pahle list mein convert karo 
# and then changes apply karo and then again wapas tuple mein convert karo. 

# access tuple item

a= (1,2,3,4,5,6,7,8)

print(a[1])  # 2
print(a[2:5]) #(3,4,5)
print(a[:4])  #(1,2,3,4)
print(a[3:])  # (4,5,6,7,8)
print(a[-4:-1]) #(5,6,7)


# Update Tuple

x= (2,5,1,3,10,0)
y=list(x)
y[1]=8
x= tuple(y)
print(x)  #(2, 8, 1, 3, 10, 0)

# del keyword with tuple

b= (1,2,3)
del b
# print(b)   # will return error that b is not defined since b alraedy deleted


# unpack Tuple

t= (1,2,3)
(m,n,q)= t
print(m) #1
print(n)  #2
print(q)  #3

# unpack tuple with astrick in tuple
 
t1 = (1,2,3,4,5,6)
(x,y,*z) =t1
print(x) #1
print(y) #2
print(z) #[3,4,5,6]  # return list type
print(type(z))

t2 =(1,2,3,4,5,6,"7",8)
(x1,*y1,z1,z2)= t2
print(x1)   #1
print(y1)   #[2,3,4,5,6]
print(z1)   #7
print(type(z2))  # str
print(z2)   #8
print(type(z2))   # int
