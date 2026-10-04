# function Argument

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Number of arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")  # if two aregument define then parameter should be two else it will thgrow error


# default parameter values

def my_function(name="world"):
  print("hello", name)

my_function("msd") 
my_function("vk")
my_function()  # here only gives hello world
my_function("rs")


def my_function1(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function1(animal = "dog", name = "Buddy")  # here argument order doesnt matter
my_function1("dog","Buddy")  #  now order matter
my_function1("Buddy","dog")  #  now order matter



def new_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

new_function("dog", name = "Buddy", age = 5)
#new_function( name = "Buddy","dog", age = 5) # here it will throw error due tp positional arguments