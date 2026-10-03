# for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("normal",x)

# braek Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print("break",x)
  if x == "banana":
    break
  

# continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print("continue",x)


  # nested for loops

  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)