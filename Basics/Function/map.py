
def squre(x):
    return x*x

print(squre(3))
print(squre(4))
print(squre(5))


# suppose we have list or array of number then want to squre the each number and return a new list/array

x=list(map(squre,[1,2,3,4,5,6]))

numberList= [11,12,13,14,15]
y=list(map(squre,numberList))

print(x)
print(y)

# map with Lambda function

numList= [9,8,7,6,5,4,3,2,1]

z=list(map(lambda x: x*x,numList))
print(z)

# add two list ||| map multiple itrable

num1= [1,2,3]
num2= [4,5,6]

added_number=list(map(lambda a,b: a+b,num1,num2))
print(added_number)


# using map function convert a string list into the integer

str_numb= ["1","2","3","4"]
int_numb= list(map(int,str_numb))
print(int_numb)

# ["apple","pomegranate",grapes,banana]  ====> ["APPLE","POMEGRANATE","GRAPES","BANANA"]

words= ["apple","pomegranate","grapes","banana"]

upper_words= list(map(str.upper,words))
print(upper_words)



data= [
  { "name": "Aarav Sharma", "age": 24 },
  { "name": "Diya Patel", "age": 29 },
  { "name": "Kabir Verma", "age": 31 },
  { "name": "Ananya Iyer", "age": 22 },
  { "name": "Vivaan Reddy", "age": 35 },
  { "name": "Ishani Choudhury", "age": 27 },
  { "name": "Arjun Malhotra", "age": 40 }
]

def getName(data):
    return data['name']

print(list(map(getName,data)))

# above example with lambda function 
names= list(map(lambda person:person["name"],data))

print(names)