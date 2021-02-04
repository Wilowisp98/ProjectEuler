# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Comments Section:
# - It can be easily done knowing that every pythagorean triplet goes by: (m^2-n^2, 2*m*n, m^2 + n^2)

def problem9():
    for i in range(1,999):
        for j in range(i,999):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                return i*j*k
