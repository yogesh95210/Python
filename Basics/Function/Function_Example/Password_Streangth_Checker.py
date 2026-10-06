# Password Straength checker

def pass_Streangth_checker(password):
   if len(password)<8:
      return "Password length should be minimum 8"
   if not any(char.isdigit() for char in password):
      return "contain atleast one digit in password"
   if not any(char.islower() for char in password):
      return "Contain atleast one smaller alphabet"
   if not any(char.isupper() for char in password):
      return "contain atleast one capital alphabet"
   if not any(char in "!@#$%^&*()_" for char in password):
      return "contain atleast one special char"
   return "Your Password is Strong"



# --- RUNNING THE TESTS ---
print(pass_Streangth_checker("Ab1!"))         # Output: Password length should be minimum 8
print(pass_Streangth_checker("ABCDEFGH1!"))   # Output: Contain atleast one smaller alphabet
print(pass_Streangth_checker("abcdefgh1!"))   # Output: contain atleast one capital alphabet
print(pass_Streangth_checker("Abcdefgh1!"))   # Output:  Your Password is Strong