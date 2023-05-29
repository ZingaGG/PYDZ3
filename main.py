# Task 1

# import random

# A = []

# n = int(input("Enter N = "))

# x = int(input("Enter X = "))

# for i in range(n):
#     A.append(random.randint(1,7))

# print(*A)

# print(len([el for el in A if x == el]))

# Task 2

# import random

# A = []

# n = int(input("Enter N = "))

# x = int(input("Enter X = "))

# Close = 0

# for i in range(n):
#    A.append(random.randint(1,7))

# print(*A)

# if A[0] < x:
#     Close = x - A[0]
# else:
#     Close = A[0] - x

# Result = 0

# for el in A:
#     if el < x:
#         if (x - el) < Close:
#             Close = x - el
#             Result = el
#         elif x - el == 0:
#             Result = el
#             break
#     else:
#         if (el - x) < Close:
#             Close = el - x
#             Result = el
#         elif x - el == 0:
#             Result = el
#             break

# print(Result)
