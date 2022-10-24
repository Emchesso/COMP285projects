import validate

def fibonacci_linear(n):
    # basic iterative function for finding fibonacci values
    validate(n)
    if n <= 1:
        return n # returns base case of 0 or 1
    previous = 0
    fibNum = 1 # initialize two values as the first two numbers in the fibonacci sequence, 0 and 1
    for _ in range(2, n + 1): # loop used to calculate the fibonacci number at place "n"
        previous, fibNum = fibNum, previous + fibNum
        # previous = fibNum # holds the previously calculated fibonacci number
        # fibNum = previous + fibNum # calculates the next fibonacci number in the sequence
    return fibNum