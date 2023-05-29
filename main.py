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

# Task 3

# Scrabble = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
#      "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

# Word = input("Enter your word = ").upper()

# Result = 0

# for letter in Word:
#     for key in Scrabble:
#         if letter == key:
#             Result += Scrabble[key]

# print(Result)    

