"""
x=5
y= "Virat"

print(x)
print(y)

# <----------------->
x= str(3)
y= int(3)
z= float(3)

print(x)
print(y)
print(z)

# <----------------->
# we can assign multiple variables
m,n,p= 1,2,3

print(m)
print(n)
print(p)

# <----------------->
# one value to multiple variables

q=w=e = "MSdhoni"

print(q)
print(w)
print(e)


# Global Variables

# Variables that are craeted outside of a function are known as global variable

u= 'awesome'

def myFunc():
    print("Python is "+u)

myFunc()
"""
# new way

x= "qwertyu"

def myFunc1():
    x="asdfgh"
    print("inside function " + x)

myFunc1()

print("Outside function " + x)


y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y)



#Global Variable

def func():
   global k
   k = "fantastic"

func()
print("Python is "+ k)


d="Virat"
def newFunc():
   global d
   d="MSD"
newFunc()
print("Hi "+ d)