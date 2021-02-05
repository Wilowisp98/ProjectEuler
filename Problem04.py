# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Comments Section:
# - Straight forward algorithm.

def ispalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

def problem4():
    palindromes = []
    for i in range(100,1000):
        for j in range(100,1000):
            if ispalindrome(i*j) is True:
                palindromes.append(i*j)
    return max(palindromes)

    
    
            
