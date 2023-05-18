import time

#Calculate the n-th term of the Fibonacci sequence using recursion
def fibonacci_rec(n):
    if n < 0 or isinstance(n, float):
        print('To calculate the n-th term of Fibonacci sequence, it must be a natural number. '
              '\nTry with whole numbers greater than or equal to zero!')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        response = fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
        return response


#The iterative version to calculate the n-th term of the Fibonacci sequence

def fibonacci_it(n):
    response = n
    a, b = 0, 1
    for k in range(2, n + 1):
        response = a + b
        a, b = b, response
    return response

#Optimizing processing time using memoization
#This technique stores results of function calls and returns cached results when the function is called again

memo = dict()
def fibonacci_mem(n):
    if n < 2:
        return n
    elif memo.get(n) != None:
        return memo[n]
    else:
        memo[n] = fibonacci_mem(n - 1) + fibonacci_mem(n - 2)
        return memo[n]

#Comparing processing time among recursion, iteration, and memoization

n = 35

start = time.time()
print(fibonacci_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))

start = time.time()
print(fibonacci_it(n))
print('Iterative: {} seconds'.format(time.time() - start))

start = time.time()
print(fibonacci_mem(n))
print('Memoization: {} seconds'.format(time.time() - start))