# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Comments Section:
# - The sum of the squares can be written as (N^2)*((N+1)^2)*1/4
# - The square of the sum can be written as N*(N+1)*(1+N*2)/6

def problem6():
    sumofsqrs = (100**2)*((101)**2)*1//4
    sqrofsums = (100*101*201)//6
    return sumofsqrs - sqrofsums
