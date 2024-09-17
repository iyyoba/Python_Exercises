#Exercise 3
def gallon_to_litre(gallons):
 return gallons * 3.76
volume_in_gallons = float(input("Enter volume in gallons: "))
while volume_in_gallons >= 0:
    print(f"Volume is {gallon_to_litre(volume_in_gallons): .3f} in litres.")
    break