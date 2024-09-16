#Exercise 4
Year = int(input("Enter a year: "))
if (Year % 4 == 0) and (Year % 100 != 0):
    print(str(Year) + " is a leap year")
elif (Year %400 == 0) and (Year % 100 == 0):
    print(str(Year) + " is a leap year.")
else:
    print(str(Year) + " is not a leap year.")