### Fibonacci Sequence
# The Fibonacci sequence is a sequence of numbers where a number is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Goal: Write function to return nth number in Fibonacci sequence.
# Example: fibonacci(4) should return 3

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    """
    Returns the nth number in the Fibonacci sequence.
    n int > 0
    returns Fibonacci number
    """
# Check that the input is a positive integer
    if type(n) != int:
        raise TypeError('n must be a positive integer')
    if n < 1:
        raise ValueError('n must be a positive integer')
    
    # Compute the Nth term
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print('Range 1-50:')
for n in range(1, 51):
    print(n, ":", fibonacci(n))

print('--------------')
print('Range 1-100:')
for n in range(1, 101):
    print(n, ":", fibonacci(n))

