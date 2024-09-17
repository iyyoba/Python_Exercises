# Exercise 5
def list(old_list):
    new_list = []
    for i in old_list:
        if i % 2 == 0:
            new_list.append(i)
    print("Old list is: ", old_list)
    print("New list is: ", new_list)
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(old_list)



