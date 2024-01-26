# Write a program that:
  # Asks for the user’s name.
  # Asks the user to input a number between 1 and 5.
  # Outputs a personalised fortune/message (that includes the user’s name) depending on which number they picked.

name = input("what is your name")
number = input("pick a number between 1-5")
if number == "1":
  print(name + " Drake will message you in 6 hours")

if number == "2":
  print(name + " You will run into a fortune soon")

if number == "3":
  print(name + " You will have good health")

if number == "4":
  print(name + " You will encounter an adventure")

if number == "5":
  print(name + " You will get signed by the toronto raptors")

