#Exercise 5
Talents = float(input("Enter talents: "))
Pounds = float(input("Enter pounds: "))
Lots = float(input("Enter lots: "))
    #One talent is 20 pounds.
    #One pound is 32 lots.
    #One lot is 13,3 grams.
lots_in_grams = Lots * 13.3
pounds_in_grams = Pounds * 13.3 * 32
talent_in_grams = Talents * 13.3 * 32 * 20
Total = talent_in_grams + pounds_in_grams + lots_in_grams
kilograms = int(Total / 1000)
grams = Total - (kilograms * 1000)
print("The weight in modern system is: ")
print(str(kilograms) + " kilograms and " + str(grams) + " grams." )