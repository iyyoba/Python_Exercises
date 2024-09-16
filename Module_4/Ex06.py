# Exercise 6
import random
points_to_generate = int(input("Enter number of points to generate: "))

n = 1
N = 1

for i in range(points_to_generate):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    if (rand_x**2 + rand_y**2) <= 1:
        n = n + 1


    N = N + 1

    Pi = 4 * n / N

print("Estimation of pi is:", Pi)
