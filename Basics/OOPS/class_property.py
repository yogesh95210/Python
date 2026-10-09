class City:
    def __init__(self,country,city):
        self.country= country
        self.city=city

C1= City("France","peris")

print(C1.country)
print(C1.city)

# Change the property

C1.country= "Sweden"
C1.city= "Amsterdam"

print(C1.country)
print(C1.city)

# Class property vs instance property:
#Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


# modifying class property

class Person:
   lastName= "sharma"

   def __init__(self,name):
      self.name= "Rohit"

p1= Person("Virat")
p2= Person("MSD")

Person.lastName= "Gupta"

print(p1.lastName)      
print(p2.lastName)   


# Adding new Properties

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)