
def checkEven(number):
    if number%2==0:
        return True
    else:
        return False
    
print(checkEven(10))
print(checkEven(7))


numList= [1,2,3,4,5,6,7,8,9]

def checkEvenNumber(num):
    if num%2==0:
        return num
    
print(list(filter(checkEvenNumber,numList)))

# filter with lambda function

greater_Than_Five= list(filter(lambda x:x>5,numList))
print(greater_Than_Five)

# with multiple condition

even_and_greater_than_five= list(filter(lambda x: x>5 and x%2==0, numList))
print(even_and_greater_than_five)

# filter out age is grater than 25

data= [
  { "name": "Aarav Sharma", "age": 24 },
  { "name": "Diya Patel", "age": 29 },
  { "name": "Kabir Verma", "age": 31 },
  { "name": "Ananya Iyer", "age": 22 },
  { "name": "Vivaan Reddy", "age": 35 },
  { "name": "Ishani Choudhury", "age": 27 },
  { "name": "Arjun Malhotra", "age": 40 }
]

def age_greater_than_25(person):
    return person["age"]>25

fiter_age_greater_than_25= list(filter(age_greater_than_25,data))
print(fiter_age_greater_than_25)