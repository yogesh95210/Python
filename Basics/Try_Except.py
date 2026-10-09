#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling

##The try block will generate an error, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")


  #  ##########

  #The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# with else  try except

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")  # will print
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") # will print



  # Finally with try execept

  #The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong !!!")
finally:
  print("The 'try except' is finished !!!!!")

