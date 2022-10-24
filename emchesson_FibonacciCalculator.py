#
# Ethan M. Chesson
# COMP 285
# Leflore
# 8/3/2022
# Fibonacci Calculator
#

# An application for calculating a Fibonacci number for a user input value.
# User may select which type of algorithm is used to calculate this, 
# and will see the average runtime after 1,000,000 iterations using that algorithm.

from time import perf_counter_ns
import timeit

class FibonacciDynamicRecursion:
    def __init__(self):
        self.memory = [0,1] # initializes object with first two Fibonacci numbers
    
    def __call__(self, n):
        '''Class method for calculating the Fibonacci number at position 'n' using a dynamic recursive algorithm'''
        if n < len(self.memory):
            return self.memory[n] # returns base case of 0 or 1, or previously calculated results from memory
        else:
            fibonacciNumber = self(n - 1) + self(n - 2) # recursive call using the next two lower Fibonacci values
            self.memory.append(fibonacciNumber) # adds calculated number to memory to later be called dynamically as a base case
        return self.memory[n]

class FibonacciDynamicLinear:
    def __init__(self):
        self.memory = [0,1]

    def __call__(self, n):
        '''Class method for calculating the Fibonacci number at position 'n' using a dynamic linear algorithm'''
        if n < len(self.memory):
            return self.memory[n] # returns base case of 0 or 1, or previously calculated results from memory
        else:
            previousNum = self.memory[0]
            currentNum = self.memory[1] # initialize two values as the first two numbers in the Fibonacci sequence, 0 and 1
            for _ in range(2, n + 1): # loop used to iterate through the Fibonacci values up to position "n"
                previousNum, currentNum = currentNum, previousNum + currentNum
                self.memory.append(currentNum) # adds calculated number to memory to later be called dynamically
        return  self.memory[n]

def validate(n):
    '''Method to ensure that the number used to call the Fibonacci functions is valid'''
    if not(isinstance(n, int) and n >= 0):
        raise ValueError(f'Expected positive integer, instead got "{n}"')

def get_fibonacci_recursion(n):
    '''Method for finding Fibonacci values using a recursive algorithm'''
    if n <= 1:
        return n # returns base case of 0 or 1
    return get_fibonacci_recursion(n - 1) + get_fibonacci_recursion(n - 2) # recursive call using the next two lower Fibonacci values

def get_fibonacci_linear(n):
    '''Method for finding Fibonacci values using a linear algorithm'''
    if n <= 1:
        return n # returns base case of 0 or 1
    previousNum = 0
    currentNum = 1 # initialize two values as the first two numbers in the Fibonacci sequence, 0 and 1
    for _ in range(2, n + 1): # loop used to iterate through the Fibonacci values up to position "n"
        previousNum, currentNum = currentNum, previousNum + currentNum
    return currentNum

def get_fib_recur_runtime():
    '''Method for recording the average runtime of the get_fibonacci_recursion method'''
    recursionSetup = '''from __main__ import get_fibonacci_recursion, numToCalc'''
    recursionCode = '''get_fibonacci_recursion(numToCalc)'''
    iterations = 1000000
    runtime = float(timeit.timeit(setup = recursionSetup, 
    stmt = recursionCode,
    number = iterations,
    timer = perf_counter_ns))
    return runtime/iterations # returns average runtime for a single iteration

def get_fib_dyn_recur_runtime():
    '''Method for recording the average runtime of the get_fibonacci_dynamic_recursion method'''
    dynamicRecursionSetup = '''from __main__ import FibonacciDynamicRecursion, numToCalc
fibonacciDynRecurObject = FibonacciDynamicRecursion()'''
    dynamicRecursionCode = '''fibonacciDynRecurObject(numToCalc)'''
    iterations = 1000000
    runtime = float(timeit.timeit(setup = dynamicRecursionSetup, 
    stmt = dynamicRecursionCode,
    number = iterations,
    timer = perf_counter_ns))
    return runtime/iterations # returns average runtime for a single iteration

def get_fib_line_runtime():
    '''Method for recording the average runtime of the get_fibonacci_linear method'''
    linearSetup = '''from __main__ import get_fibonacci_linear, numToCalc'''
    linearCode = '''get_fibonacci_linear(numToCalc)'''
    iterations = 1000000
    runtime = float(timeit.timeit(setup = linearSetup, 
    stmt = linearCode, 
    number = iterations, 
    timer = perf_counter_ns))
    return runtime/iterations # returns average runtime for a single iteration

def get_fib_dyn_line_runtime():
    '''Method for recording the average runtime of the get_fibonacci_dynamic_linear method'''
    dynamicLinearSetup = '''from __main__ import FibonacciDynamicLinear, numToCalc
fibonacciDynLineObject = FibonacciDynamicLinear()'''
    dynamicLinearCode = '''fibonacciDynLineObject(numToCalc)'''
    iterations = 1000000
    runtime = float(timeit.timeit(setup = dynamicLinearSetup, 
    stmt = dynamicLinearCode, 
    number = iterations,
    timer = perf_counter_ns))
    return runtime/iterations # returns average runtime for a single iteration

if __name__ == '__main__':
    programLoop = True
    while(programLoop): # prints menu options for program
        print('''Welcome to the Fibonacci Calculator, which algorithm would you like to use?
        1) Recursion
        2) Dynamic Recursion
        3) Linear
        4) Dynamic Linear
        5) Use all algorithms and compare runtime results
        6) Exit
        ''')
        option = int(input("Selection number: "))
        if (option == 6):
            print("Thank you for using Fibonacci Calculator, goodbye.\n")
            programLoop = False
            break
        numToCalc = int(input("Enter the number of the Fibonacci sequence you would like to calculate: "))
        validate(numToCalc)
        print()
        if (option == 1):
            runtimeRecur = get_fib_recur_runtime()
            fibNumRecur = get_fibonacci_recursion(numToCalc)
            print(f'The {numToCalc}th Fibonacci number is {fibNumRecur}')
            print(f'It took an average of {runtimeRecur} nanoseconds to calculate this using a recursive method.\n')
        elif (option == 2):
            runtimeDynRecur = get_fib_dyn_recur_runtime()
            fibDynRecurObj = FibonacciDynamicRecursion()
            fibNumDynRecur = fibDynRecurObj(numToCalc)
            print(f'The {numToCalc}th Fibonacci number is {fibNumDynRecur}')
            print(f'It took an average of {runtimeDynRecur} nanoseconds to calculate this using a dynamic recursive method.\n')
        elif (option == 3):
            runtimeLine = get_fib_line_runtime()
            fibNumLine = get_fibonacci_linear(numToCalc)
            print(f'The {numToCalc}th Fibonacci number is {fibNumLine}')
            print(f'It took an average of {runtimeLine} nanoseconds to calculate this using a linear method.\n')
        elif (option == 4):
            runtimeDynLine = get_fib_dyn_line_runtime()
            fibDynLineObj = FibonacciDynamicLinear()
            fibNumDynLine = fibDynLineObj(numToCalc)
            print(f'The {numToCalc}th Fibonacci number is {fibNumDynLine}')
            print(f'It took an average of {runtimeDynLine} nanoseconds to calculate this using a dynamic linear method.\n')
        elif (option == 5):
            runtimeRecur = get_fib_recur_runtime()
            runtimeDynRecur = get_fib_dyn_recur_runtime()
            runtimeLine = get_fib_line_runtime()
            runtimeDynLine = get_fib_dyn_line_runtime()
            fibNumLine = get_fibonacci_linear(numToCalc)
            print(f'The {numToCalc}th Fibonacci number is {fibNumLine}')
            print(f'''
            The average runtimes for each algorithm in nanoseconds are:
            \tRecursion: {runtimeRecur}
            \tDynamic Recursion: {runtimeDynRecur}
            \tLinear: {runtimeLine}
            \tDynamic Linear: {runtimeDynLine}
            ''')
        else:
            print("Invalid entry, please select from the menu.")

    '''Code used to create the presentation graphs, no longer used'''
    # runtimesRecursion = {}
    # runtimesDynamicRecursion = {}
    # runtimesLinear = {}
    # runtimesDynamicLinear = {}
    # for i in range(16):
    #     runtimesRecursion[i] = get_fib_recur_runtime()
    # for j in range(16):
    #     runtimesDynamicRecursion[j] = get_fib_dyn_recur_runtime()
    # for k in range(16):
    #     runtimesLinear[k] = get_fib_line_runtime()
    # for l in range(16):
    #     runtimesDynamicLinear[l] = get_fib_dyn_line_runtime()
    # print("Recursion runtimes:", runtimesRecursion)
    # print("Dynamic Recursion runtimes:", runtimesDynamicRecursion)
    # print("Linear runtimes:", runtimesLinear)
    # print("Dynamic Linear runtimes:", runtimesDynamicLinear)
