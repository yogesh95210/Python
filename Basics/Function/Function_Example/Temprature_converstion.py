

# Temperature conversion function

def tempConversion(temperature,unit):
    """this function converts temprature between Celsius and Farhenhite """
    if unit== "C":
        return temperature *9/5 +32  # C to F
    elif unit== "F":
        return (temperature-32) *5/9
    else:
        return None

print(tempConversion(26,"C"))
print(tempConversion(77,"F"))
print(tempConversion(28,""))