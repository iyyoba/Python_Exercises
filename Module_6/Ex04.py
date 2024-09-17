#Ex04
def sum(int_list):
    result = 0
    for i in int_list:
     result += i
    return result
int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 100]
print("Sum of the numbers is: ", sum(int_list))