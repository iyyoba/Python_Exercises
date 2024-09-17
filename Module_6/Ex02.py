# Exercise 2
import random
def dice_roll(sides):
    return random.randint(1, sides)
number_sides = int(input("Number of sides on the dice: "))
number = dice_roll(number_sides)
while number != number_sides:
    print(number)
    number = dice_roll(number_sides)
print(number)