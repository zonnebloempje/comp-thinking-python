import sys
print('RECURSION LIMIT:')
print(sys.getrecursionlimit())

def factorial(n):
    """
    Calcula el factorial de n. 
    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Write an integer: '))

print(factorial(n))