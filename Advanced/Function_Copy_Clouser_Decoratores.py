
def Welcome():
    print("Hi Python World!!")

Welcome()

wel= Welcome
wel()

del Welcome  # del keyword will not work this way in function
wel()  # here it will invoke and print the string in function 



# Closures in Python

def main_func():
    msg="Welcome"
    def sub_main_func():
        print('Rohit')
        print(msg)   # here we can access the variable from outside of this function
        print('Virat')
    return sub_main_func()

main_func()


def Outer():
    message= "Hi Rohit"

    def inner():
        print(message)
    
    return inner


my_func = Outer()
my_func()


def multiplier(x):
    def multiply(y):
        return x * y
    
    return multiply

double= multiplier(2)
triple= multiplier(3)

print(double(2))
print(triple(3))


def outer():
    x = 10

    def inner():
        return x + 5

    return inner

func = outer()
print(func())



# Decoratores

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


def greet():
    print("Hello Rohit")


greeting = my_decorator(greet)
greeting()