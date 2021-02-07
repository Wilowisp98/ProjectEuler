# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# Comments Section:
# - Working with the remainder

num1to20 =  ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

num20to90 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def problem17():
    counter = 0
    for i in range(1,1001):
        counter += len(str(numtoword(i)))
    return counter

def numtoword(n):
    if n < 20:
        return num1to20[n-1]
    if 20 <= n <=99:
        return num20to90[n//10 - 2] + (num1to20[n%10 - 1] if (n%10 != 0) else "")
    if 100 <= n <= 999:
        return num1to20[n//100 - 1] + "hundred" + (("and" + numtoword(n%100)) if (n%100 != 0) else "")
    if n == 1000:
        return "onethousand"

