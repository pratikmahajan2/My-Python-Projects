import random
my_number = random.randint(0,100)
print("Please guess my number - between 0 and 100: ")

while True:
  your_number = int(input(""))
  if your_number > 100 or your_number < 0:
    print("Ohhoo! You need to enter number between 0 and 100. Try again")
  elif (your_number > my_number):
    print("Your guess is greater than my number. Try again")
  elif (your_number < my_number):
    print("Your number is less than my number. Try again" )
  else:
    print("Your won. My number is: ", my_number)
    break
  