
# if we dont know how many argument will we passed in fumction then we should add * in function parmater as below

def myFunction(*param):
    print(param[2])
    print(param[3])
    print(param[4])
    print(type(param[4]))

myFunction(10,20,30,40,"fifty",60,70)


def my_func(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
  print("all argumnet type:", type(args))   #this is tuple type

my_func("Emil", "Tobias", "Linus")


# we can combine regular parameter with *args

def func1( greeting,*names):
   print("greet",greeting)
   print("names",names)
   for name in names:
      print(name)

func1("Hello", "Emil", "Tobias", "Linus")



# write a function that calculate the sum of any given numbers

def calculateSum(*number):
   total=0
   for num in number:
      total += num
   return total

print(calculateSum(1,2,3,4,5))
print(calculateSum(10,20,30,40,50))
print(calculateSum(5))
print(calculateSum(550))


# write a function to find the maximum value
# maximum value
def func2(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(func2(3, 7, 2, 9, 1))



# Arbitrary Keyword Arguments - **kwargs

def func3(**kid):
  print(type(kid))
  print(kid)
  print("His last name is " + kid["lname"])
  print("His firstname name is " + kid["fname"])
func3(fname = "Tobias", lname = "Refsnes")


def func4(**myvar):
  print("Type:", type(myvar))  # dict
  print("Name:", myvar["name"]) # Tobias
  print("Age:", myvar["age"])   # 30
  print("All data:", myvar)    # {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

func4(name = "Tobias", age = 30, city = "Bergen")

# we can combine **kwargs with Regular Arguments

def func5(username,**details):
   print("Username:", username)
   print("Additional details:")
   for key, value in details.items():
    print(" ", key + ":", value)
   
func5("emil123", age = 25, city = "Oslo", hobby = "coding")


# combining *args and **kwargs

# Order must be regular parameter ---> *args ----> **kwargs

def Myfunc(title,*args,**kwargs):
  print("Title: ", title)
  print("Positional arguments: ", args)
  print("keywords arguments: ", kwargs)

Myfunc("User Info","email","MSD", age= 40, city="Ranchi")


# Unpacking Arguments

# Unpacking list with *
def myfunc6(a,b,c):
  return a+b+c

input= [1,2,3]
result= myfunc6(*input)   #yaha input (list type hain) ko unpack karke argument mein bhej raha hain
print(result)

# unpacking Dict with **  (dictionary will unpack with **)

def my_function3(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function3(**person) # Same as: my_function(fname="Emil", lname="Refsnes")



