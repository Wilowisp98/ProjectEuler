from itertools import permutations

def problem24():
    perms = list(permutations([0,1,2,3,4,5,6,7,8,9]))
    return perms[999999]
