# Exercise 1
import random
def dice_roll():
    return random.randint(1, 6)
number = dice_roll()
while number != 6:
    print(number)
    number = dice_roll()
print(number)