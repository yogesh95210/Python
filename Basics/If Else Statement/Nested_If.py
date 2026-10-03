
# Nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


age= 25
has_licence= False

if age>18:
  if has_licence:
    print("Please drive")
  else:
    print("Please get Licence")
else:
  print("Can't Drive")