# Exercise 2
numbers_list = []
number = input(f"Enter a number: ")
while number != "":
    numbers_list.append(number)
    number = input(f"Enter a number: ")
numbers_list.sort(reverse = True)
print("The 5 greatest numbers are: ")
for i in range(5):
    print(numbers_list[i])




