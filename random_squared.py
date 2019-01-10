# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
import random

random_nums = [random.randint(0,49) for num in range(20)]
print(random_nums)

# With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].
random_nums_squared = [random_nums[i] * random_nums[i] for i in range(len(random_nums))]
print(random_nums_squared)

# PRINT RESULT:
# [41, 0, 45, 3, 8, 46, 41, 2, 3, 31, 6, 34, 41, 3, 39, 42, 1, 29, 13, 26]
# [1681, 0, 2025, 9, 64, 2116, 1681, 4, 9, 961, 36, 1156, 1681, 9, 1521, 1764, 1, 841, 169, 676]