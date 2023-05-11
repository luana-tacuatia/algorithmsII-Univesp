#Calcuate the factorial of a number using recursion

def factorial(n):
    if n < 0 or isinstance(n, float):
        print("To calculate the factorial of a number, it must be a natural one. "
              "\nTry with whole numbers greater than or equal to zero!")
    elif n == 0:
        return 1
    else:
        response = n * factorial(n - 1)
        return response

