# Exercise 6
import math
def cal_price(diam, price, name):
    pizza_area = math.pi * (diam/2)**2
    return price / pizza_area

diam1 = float(input("Enter the diameter of 1st pizza: "))
diam2 = float(input("Enter the diameter of 2nd pizza: "))
price1 = float(input("Enter the price of the 1st pizza: "))
price2 = float(input("Enter the price of the 2nd pizza: "))

if cal_price(diam1, price1, 1) > cal_price(diam2, price2, 2):
    print(" 1st pizaa is more expensive.")
elif cal_price(diam1, price1, 1) < cal_price(diam2, price2, 2):
    print ("1st pizaa is cheaper.")
else:
    print("Equal priced.")





