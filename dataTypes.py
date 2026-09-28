#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType


x= "Rohit"   #string
print(type(x))
x=20   #Int
print(type(x))
x=20.5 #float
print(type(x))
x=1j   #Complex
print(type(x))
x=["a","b","c"] #List
print(type(x))
x=("a","b","c") #tuple
print(type(x))
x= range(6) #range
print(type(x))
x = {"name" : "John", "age" : 36} #dict
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = True
y=False
print(type(x))
print(type(y))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))


