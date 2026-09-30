x = 5

x += 3        # x becomes 8
print(x)      # Prints: 8

x -= 3        # x becomes 5 (8 - 3)
print(x)      # Prints: 5

x *= 3        # x becomes 15 (5 * 3)
print(x)      # Prints: 15

x /= 3        # x becomes 5.0 (15 / 3) -> Note: Division always returns a float
print(x)      # Prints: 5.0

# We can write above code in following pattern as well

"""
x = 5

print(x := x + 3)  # Assigns x = 8 and prints: 8
print(x := x - 3)  # Assigns x = 5 and prints: 5
print(x := x * 3)  # Assigns x = 15 and prints: 15
print(x := x / 3)  # Assigns x = 5.0 and prints: 5.0

"""