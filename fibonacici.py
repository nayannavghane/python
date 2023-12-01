#Write a Python function that generates the first n numbers of the Fibonacci sequence, where n is taken as input.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones
# starting from 0 and 1.

def fib(n):
    a = 0
    b = 1
    if n == 0:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(0)