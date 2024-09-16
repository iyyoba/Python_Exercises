# Exercise 1
import random
num_dice = int(input("How many dices do you want? "))
sum_rolls = 0
for i in range(num_dice):
    dice_roll = random.randint(1, 6)
    sum_rolls += dice_roll
print("Sum of the roll results is", sum_rolls)




