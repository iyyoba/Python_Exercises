# Exercise 3
number = int(input("Enter a number: "))
if number > 1:
 for i in range(2, (number //2)+1):
    if (number % i) == 0:
        print("Your number is not a prime number.")
        break
 else:
    print("Your number is a prime number.")
else:
    print("Your number is not a prime number.")

