
# Elif Statement

# Elif Keyword

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Multiple Elif Statment

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#  Note  ---->  Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.