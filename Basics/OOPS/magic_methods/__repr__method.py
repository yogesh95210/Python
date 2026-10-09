
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

  def __repr__(self):
    return f"Personss(name={self.name!r}, age={self.age})"

p1 = Person("Rohit", 38)

print(p1)
print(repr(p1))
