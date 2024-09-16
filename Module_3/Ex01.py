# Exercise 1
length = float(input('Enter the length in centimeters: '))
length_shortfall = 42 - length
if length < 42:
    print("Please release the fish back to the lake. ")
    print("The fish is " + str(length_shortfall) + " centimeters shorter than the requirement.")