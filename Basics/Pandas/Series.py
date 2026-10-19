import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["x"])
print(myvar["y"])
print(myvar["z"])

# key/value object in series

calories = {"day1": 420, "day2": 380, "day3": 390}
myData= pd.Series(calories)
print(myData)

####

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


# DataFrame

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

newData = pd.DataFrame(data)
print(newData)

