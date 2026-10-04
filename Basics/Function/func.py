#define  function 
def myFunc():
    print("MSD")

# calling function
myFunc()

# we can call function multiple times

myFunc()
myFunc()
myFunc()
myFunc()


#  Write a function that convert the farenhite temp into celsius

def tempChange(temp):
    return (temp-32) * 5/9

print(tempChange(77))
print(tempChange(95))
print(tempChange(50))


# return value

def greetFunc():
    return "Welcome to the python world!"

message= greetFunc()

print(message)

