# Exercise 4
import random
number = int(random.randint(1, 10))
#guess = int(input(" Enter your guess: "))
while True:
  guess = int(input("Make a guess: "))
  if guess == number:
      print("Correct!")
      break
  if guess < number:
   print("Too low!")
  elif guess > number:
    print("Too High!")
