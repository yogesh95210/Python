# without __str__(), printing an object shows its memory address:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

#

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):     # this must return a string else throw type error
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 25)
print(p1)