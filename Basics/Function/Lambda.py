# Syntex ---->  lambda arguments : expression

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.


x= lambda a: a+10
print(x(5))

y= lambda a,b: a+b
print(y(10,20))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))