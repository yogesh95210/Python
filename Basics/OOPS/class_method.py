class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))



# method accesing property

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())


# method Modifying Properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):     # method to increse the age
    self.age +=1
    print(f"Happy Birthday! you are now {self.age}")


p1= Person("MSD",45)

p1.celebrate_birthday()
p1.celebrate_birthday()