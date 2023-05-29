# Task 1

import random

A = []

n = int(input("Enter N = "))

x = int(input("Enter X = "))

for i in range(n):
    A.append(random.randint(1,7))

print(*A)

print(len([el for el in A if x == el]))

