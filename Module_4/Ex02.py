# Exercise 2
length_in_inches = float(input("Enter a length in inches: "))
length_in_centimeters = length_in_inches / 2.54
while length_in_inches > 0:
    print(f"The length is  {length_in_centimeters: 2.2f} centimeters.")
    break