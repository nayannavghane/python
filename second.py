# take input form user a string and check if it is palindrome or not
username = input("what is your name? ")
if(username==username[::-1]):
  print("The string is a palindrome")
else:
  print("Not a palindrome")
