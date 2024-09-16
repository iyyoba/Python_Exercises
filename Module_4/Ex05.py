# Exercise 5
Username = "Python"
Password = "rules"
number_of_tries = 0
while number_of_tries < 5:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if entered_username == Username and entered_password == Password:
        print("Welcome!")
        break
    number_of_tries = number_of_tries + 1
else:
 print("Access Denied!")

