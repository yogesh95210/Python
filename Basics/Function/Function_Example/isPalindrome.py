
# Write a function to check given string is palindrome

def isPalindrome(str):
   temp=""
   for s in str:
      temp = s +temp
   return temp==str


print(isPalindrome("madam"))
print(isPalindrome("racecar"))
print(isPalindrome("level"))
print(isPalindrome("hello"))


# second way

def isPalindrome2(str):
  temp= str[::-1]
  return temp== str

print(isPalindrome2("madam"))
print(isPalindrome2("racecar"))
print(isPalindrome2("level"))
print(isPalindrome2("hello"))