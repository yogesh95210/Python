 # int
x=1

# float
y=2.8

#complex
z=1+0j

print(type(x))
print(type(y))
print(type(z))


a= float(x)
b=int(y)
c=complex(x)


print(type(a))
print(type(b))
print(type(c))


real_part = c.real
img_part= c.imag

print(real_part)  #1.0
print(img_part)   #0.0



import random

print(random.randrange(1, 10))
