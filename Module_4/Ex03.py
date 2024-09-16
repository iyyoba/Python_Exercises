# Exercise 3
numbers = []
number = input( f"Enter a number or quit by pressing enter: ")
while number != "":
    numbers.append(number)
    number = input(f"Enter a number or quit by pressing enter: ")
numbers.sort()
print(numbers)
print("Largest number is,", max(numbers))
print("Smallest number is,", min(numbers))
