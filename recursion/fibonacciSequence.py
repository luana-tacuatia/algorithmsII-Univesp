#Calculate the n-th term of the Fibonacci sequence using recursion

def fibonacci(n):
    if n < 0 or isinstance(n, float):
        print("To calculate the nth term of Fibonacci sequence, it must be a natural one. "
              "\nTry with whole numbers greater than or equal to zero!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        response = fibonacci(n - 1) + fibonacci(n - 2)
        return response
