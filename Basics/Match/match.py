# match expression Syntex

# syntex
"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

"""

day = 5
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


# combine values or we can write with or condition using |

day=4
match day:
  case 1|2|3|4|5:
    print("Weekday")
  case 6|7:
    print("Weekend")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


