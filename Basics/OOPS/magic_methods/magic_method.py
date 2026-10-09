class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Person: {self.name}"

p1 = Person("Virat")
print(p1)


# note ===>>>  Because of the double underscores, they are also called dunder methods (short for "double underscore").


