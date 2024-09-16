# Exercise 4
city_names = []
city_name = input("Enter first city or press enter to exit: ")
while len(city_names) < 5:

    city_names.append(city_name)
    city_name = input("Enter name of a city or press enter to exit: ")
for i in city_names:
    print("City name:", city_names)
