import validate

memoryRecursive = {0:0, 1:1} # holds base case and previous call results in memory cache
def fibonacci_dynamic_recursion(n):
    # improves the speed of the recursive function by eliminating repetitive calls using the memory dict
    validate(n)
    if n in memoryRecursive:
        return memoryRecursive[n] # returns base case of 0 or 1, or previously calculated results from memory dict
    memoryRecursive[n] = fibonacci_dynamic_recursion(n-1) + fibonacci_dynamic_recursion(n-2) # recursive call, adds results to memory dict
    return memoryRecursive[n]