#  write a function to calculate factorial for give number

def factorial(number):
  if number<0:
    return "Error: Factorial of negative numbers is not defined"
  if number==0:
    return 1
  else:
    return number * factorial(number-1)

print(factorial(4))
print(factorial(3))
print(factorial(10))
print(factorial(42))
print(factorial(5))