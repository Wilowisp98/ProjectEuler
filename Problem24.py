# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Comments Section:
# - Just used itertools.

from itertools import permutations

def problem24():
    perms = list(permutations([0,1,2,3,4,5,6,7,8,9]))
    return perms[999999]
