# While Loop

i=1

while i<6:
    print(i)
    i+=1

 # with break keyword
i = 5
while i < 10:
  print("break",i)
  if i == 8:
    break
  i += 1

# with continue keyword
i = 11
while i < 16:
  i += 1
  if i == 13:
    continue
  print("continue",i)


  # with else statement

  i = 21
while i < 26:
  print("else",i)
  i += 1
else:
  print("i is no longer less than 26")