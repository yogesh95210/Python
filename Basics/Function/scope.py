# Scope in python


# Global Scope
q=10000
def newFunc():
  print(q)

newFunc()
print(q)

# Local Scope

# A variable created inside a function, is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()   # if we access the x outside of this fuction then it will throw error


# Function inside Function

# The local variable can be accessed from a function ,within the function:
def myfunc1():
  y = 300
  def myinnerfunc():
    print(y)    # we can access y here
  myinnerfunc()

myfunc1()


# if we operate same variable diffrent position in code

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()   # The function will print the local x, and then the code will print the global x:

print(x)


# global keyword

# global variable will make variable global scope we can access the global keyword variable anywhere in the code

def myfunction1():
  global m
  m = "MSD"

myfunction1()

print(m)


# nonlocal keyword

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


# The LEGB Rule

#Python follows the LEGB rule when looking up variable names, and searches for them in this order:

#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace

g = "global"

def outer():
  g = "enclosing"
  def inner():
    g = "local"
    print("Inner:", g)
  inner()
  print("Outer:", g)

outer()
print("Global:", g)