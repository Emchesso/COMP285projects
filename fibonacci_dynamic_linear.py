import validate

memoryLinear = {0:0, 1:1}
def fibonacci_dynamic_linear(n):
    validate(n)
    if n in memoryLinear:
        return memoryLinear[n] # returns base case of 0 or 1, or previously calculated results from memory dict
    previous = memoryLinear[0]
    fibNum = memoryLinear[1]
    for i in range(2, n + 1):
        previous, fibNum = fibNum, previous + fibNum
        memoryLinear[i] = fibNum
    return memoryLinear[n]