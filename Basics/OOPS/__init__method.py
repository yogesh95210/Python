# craete class using The __init__() Method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age= age

p1=Person("MSD",45)

print(p1.name)
print(p1.age)

# craete class without using The __init__() Method

class Person1:
    pass

m1=Person1()
m1.name= "Virat"
m1.age= "38"

print(m1)
print(m1.name)
print(m1.age)


#Default Values in __init__()

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


# Multipe Parameter

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)